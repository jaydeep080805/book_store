from .movie import Movie

class MovieRepository:
    def __init__(self, db):
        self._conn = db

    def all(self):
        movies = self._conn.execute("SELECT * FROM movies")
        movie_objects = []

        for movie in movies:
            # use Kwargs to unpack values
            movie_objects.append(Movie(**movie)) 
        
        return movie_objects
    
    def create(self, new_movie):
        self._conn.execute("INSERT INTO movies (title, release_year) VALUES (%s, %s)", [new_movie.title, new_movie.release_year])