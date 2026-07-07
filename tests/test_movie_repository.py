from ..lib.movies.movie_repository import MovieRepository, Movie

def test_get_all_movies(db):
    movie_repo = MovieRepository(db)

    all_movies = movie_repo.all()

    assert all_movies == [Movie("Interstellar", 2009, 1), Movie("Inception", 2009, 2)]


def test_create_adds_movie_to_db(db):
    movie_repo = MovieRepository(db)

    movie_repo.create(Movie("title", 2000, 3))

    all_movies = movie_repo.all()

    assert all_movies == [Movie("Interstellar", 2009, 1), Movie("Inception", 2009, 2), Movie("title", 2000, 3)]