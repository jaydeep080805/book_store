from flask import Blueprint, render_template, redirect, request
from lib.movies.movie_repository import MovieRepository
from lib.movies.movie import Movie
from database_connection import DatabaseConnection

movie_route = Blueprint('movie_route', __name__,
                        template_folder='templates')


@movie_route.route("/movies", methods=["GET"])
def movies():
    db_conn = DatabaseConnection()
    db_conn.connect()
    
    movie_repo = MovieRepository(db_conn)
    list_of_movies = movie_repo.all()
    
    return render_template("movies/movies.html", movies=list_of_movies)

@movie_route.route("/movies", methods=["POST"])
def create_movie():
    form_data = request.form
    title = form_data.get("title")
    release_year = form_data.get("release_year")

    db_conn = DatabaseConnection()
    db_conn.connect()
    movie_repo = MovieRepository(db_conn)
    
    # create movie and add to db
    new_movie = Movie(title, int(release_year))
    movie_repo.create(new_movie)

    return redirect("/movies")