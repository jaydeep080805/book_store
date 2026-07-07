from ..lib.movies.movie import Movie

def test_movie_has_correct_attributes():
    movie = Movie("Interstellar", 2009, 1)

    assert movie.title == "Interstellar"
    assert movie.release_year == 2009
    assert movie.id == 1


def test_movie_equality_works():
    movie = Movie("Interstellar", 2009, 1)
    movie2 = Movie("Interstellar", 2009, 1)

    assert movie == movie2


def test_movie_string_representation():
    movie = Movie("Interstellar", 2009, 1)

    assert str(movie) == f"Movie(id: {movie.id}, title: {movie.title}, release year: {movie.release_year})"