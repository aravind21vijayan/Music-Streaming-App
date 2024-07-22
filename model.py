from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class album(db.Model):
    __tablename__ = "album"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String)
    poster =db.Column(db.String)
    


class song(db.Model):
    __tablename__ = "song"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    lyrics = db.Column(db.String, nullable=False)
    audio = db.Column(db.LargeBinary)
    duration = db.Column(db.String, nullable=False)
    release_date = db.Column(db.String)
    rating = db.Column(db.Integer)
    poster =db.Column(db.String)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), default=None)
    


class users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    role =db.Column(db.String, nullable=False)

class playlist_song(db.Model):
    __tablename__ = "playlist_song"
    id=db.Column(db.Integer, db.ForeignKey('your_playlist.id'),primary_key=True)
    song_id= db.Column(db.Integer, db.ForeignKey('song.id'),primary_key=True)


class your_playlist(db.Model):
    __tablename__ = "your_playlist"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

class admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    password = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    