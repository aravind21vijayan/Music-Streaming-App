from flask import Flask , render_template ,request,redirect,url_for
from model import *
import os
from sqlalchemy import func
from sqlalchemy import and_

current_dir = os.path.abspath(os.path.dirname(__file__)) 


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(current_dir, "musicDB.sqlite3")

db.init_app(app)
app.app_context().push()


@app.route("/",methods=['POST','GET'])
def index():
    if request.method=='POST':
        value_username = request.form["username"]
        value_password= request.form["password"]
        
        if users.query.filter(and_(users.username == value_username, users.password == value_password, users.role == "user")).first():
                return redirect(url_for('home'))
        elif users.query.filter(and_(users.username == value_username, users.password == value_password, users.role == "creator")).first():
                return redirect(url_for('creator'))
       
        return  redirect(url_for('signup'))
    
    return render_template("login.html")



@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method=='POST':
        value_username =request.form["username"]
        value_password= request.form["password"]
        value_usertype=request.form["user-type"]
        if not users.query.filter(users.username == value_username).all():
                newuser=users(username=value_username,password=value_password,role=value_usertype)
                db.session.add(newuser)
                db.session.commit()
                return redirect(url_for('index'))
        return  render_template("signup.html")  
    
    
    return render_template("signup.html")


@app.route("/creator",methods=['POST','GET'])
def creator():
    if request.method =='POST':
        
        if request.form['formType']=='add_song':
            value_id = request.form["id"]
            value_name = request.form["name"]
            value_genre = request.form["genre"]
            value_artist = request.form["artist"]
            value_lyrics = request.form["lyrics"]
            value_audio = request.files["audio"].read() 
            value_duration = request.form["duration"]
            value_release_date = request.form["release_date"]
            value_poster = request.form["poster"]  
            value_album_id = request.form["album_id"]
            value_rating = request.form["rating"]
        
            newsong=song(id=value_id,name = value_name,genre = value_genre,artist = value_artist,lyrics = value_lyrics,
                        audio = value_audio,  
                        duration = value_duration,
                        release_date = value_release_date,
                        poster = value_poster,  
                        album_id = value_album_id,
                        rating=value_rating)
            db.session.add(newsong)
            db.session.commit()
            return "new song added"
        
        elif request.form['formType']=='add_album':
            value_id = request.form["id"]
            value_name = request.form["name"]
            value_genre = request.form["genre"]
            value_artist = request.form["artist"]
            value_release_date = request.form["release_date"]
            value_poster = request.form["poster"] 
            newalbum=album(id=value_id,name = value_name,genre = value_genre,artist = value_artist,release_date = value_release_date,poster = value_poster)
            db.session.add(newalbum)
            db.session.commit()
            return "new album added"

        
        
        
        elif request.form['formType']=='delete_song':
            value_title =request.form["song_name"]
            tobedeleted=song.query.filter(song.name==value_title).first()
            if tobedeleted:
                db.session.delete(tobedeleted)
                db.session.commit()
                return "song deleted"
            return "song doesn't exist"
        elif request.form['formType']=='delete_album':
            value_title =request.form["album_name"]
            tobedeleted=album.query.filter(album.name==value_title).first()
            if tobedeleted:
                db.session.delete(tobedeleted)
                db.session.commit()
                return "album deleted"
            return "album doesn't exist"
    return render_template("creator.html")
    
@app.route("/about")

def about():
    return render_template("about.html")
   


@app.route("/adminlogin",methods=['POST','GET'])
def adminlogin():
    if request.method=='POST':
        value_username =request.form["username"]
        value_password= request.form["password"]
        if not users.query.filter(users.username == value_username).all():
                newadmin=users(username=value_username,password=value_password,role="admin")
                db.session.add(newadmin)
                db.session.commit()
                return redirect(url_for('admin'))
        return  redirect(url_for('admin'))  
    
    return render_template("adminlogin.html")

@app.route("/admin",methods=['POST','GET'])
def admin():
    value_count_user = users.query.filter(users.role == 'user').count()
    value_count_creator = users.query.filter(users.role == 'creator').count()
    value_count_album=album.query.with_entities(func.count(album.id.distinct())).scalar()
    value_count_song=song.query.with_entities(func.count(song.id.distinct())).scalar()
    if request.method =='POST':
        
        if request.form['formType']=='delete':
            value_title =request.form["song_name"]
            tobedeleted=song.query.filter(song.name==value_title).first()
            if tobedeleted:
                db.session.delete(tobedeleted)
                db.session.commit()
                return "song deleted"
            return "song doesn't exist"
        elif request.form['formType']=='delete_album':
            value_title =request.form["album_name"]
            tobedeleted=album.query.filter(album.name==value_title).first()
            if tobedeleted:
                db.session.delete(tobedeleted)
                db.session.commit()
                return "album deleted"
            return "album doesn't exist"
    return render_template("admin.html",count_user=value_count_user,count_creator=value_count_creator,count_album=value_count_album,count_song=value_count_song)
  







@app.route("/latest")

def latest():
    latest=[]
    choice= song.query.all()
    for i in choice:
        if i.rating > 4.5:
            latest.append(i)
    return render_template("latest.html",show =latest )

@app.route("/playlist")
def playlist():
    
    choice= your_playlist.query.all()
    return render_template("playlist.html" ,show= choice)




@app.route("/home")
def home():
    choice= album.query.all()
    choice2= song.query.all()
    return render_template("home.html",show =choice,show2=choice2 )




@app.route("/filter_album",methods=['POST'])
def filter_album():
    
    value = request.form["searchKey"]
    searchtype =request.form['filteroption']
    
    if searchtype=='name':
        result = album.query.filter(album.name.like('%'+value+'%')).all()
    
    elif searchtype=='artist':
        result = album.query.filter(album.artist.like('%'+value+'%')).all()
    
    elif searchtype=='genre':
        result = album.query.filter(album.genre.like('%'+value+'%')).all()
    
    return render_template("filter_album.html" , data=result)


@app.route("/filter_song",methods=['POST'])
def filter_song():
    
    value = request.form["searchKey"]
    searchtype =request.form['filteroption']
    
    if searchtype=='name':
        result = song.query.filter(song.name.like('%'+value+'%')).all()
    
    elif searchtype=='rating':
        result = song.query.filter(song.rating.like(value+'%')).all()
    
    elif searchtype=='genre':
        result = song.query.filter(song.genre.like('%'+value+'%')).all()
    
    return render_template("filter_song.html" , data=result)





if __name__ == '__main__':
    db.create_all()
    app.debug= True 
    app.run(host='0.0.0.0')