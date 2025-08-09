# Music Streaming App

A simple music streaming application built with Flask.

## Description

This is a web-based music streaming application that allows users to listen to music, create playlists, and manage their own content. The application has three types of users: regular users, creators, and administrators.

- **Users** can sign up, log in, listen to songs, and create their own playlists.
- **Creators** can upload their own songs and albums, and manage their content.
- **Admins** have access to a dashboard where they can view statistics about the application and manage all content.

## Features

- User authentication (signup, login) for different roles.
- Separate dashboards for users, creators, and admins.
- Song and album management for creators and admins.
- Search functionality to filter songs and albums by name, artist, genre, or rating.
- Playlist creation for users.
- A "Latest" section for highly-rated songs.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Music-Streaming-App.git
    cd Music-Streaming-App
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: A `requirements.txt` file is not currently present. You will need to create one based on the imports in the Python files. The primary dependencies are `Flask` and `Flask-SQLAlchemy`.*

3.  **Initialize the database:**
    The application uses SQLite as its database. The database file `musicDB.sqlite3` will be created automatically when you first run the application.

4.  **Run the application:**
    ```bash
    python main.py
    ```
    The application will be accessible at `http://127.0.0.1:5000` or `http://0.0.0.0:5000`.

## File Structure

- `main.py`: The main Flask application file containing the routes and logic.
- `model.py`: Defines the database models (User, Song, Album) using SQLAlchemy.
- `templates/`: Contains the HTML templates for the different pages of the application.
- `static/`: Contains static files such as CSS, JavaScript, and audio files.
- `musicDB.sqlite3`: The SQLite database file.
- `album.csv`, `song.csv`: Sample data files (it is unclear if these are used by the application).
