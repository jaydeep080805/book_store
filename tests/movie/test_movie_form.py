from playwright.sync_api import Page, expect

def test_movie_form_loads(page: Page):
    page.goto("http://localhost:5001/movies")

    title = page.locator("h1")

    expect(title).to_have_text("Movies")


def test_movie_list_is_correct(page: Page, db):
    page.goto("http://localhost:5001/movies")

    movies = page.locator("li")
    list_of_movies = movies.all_inner_texts()

    expected_movies = ["Interstellar - 2009", "Inception - 2009"]


    # print(movies.all_inner_texts()[0].split("-"))

    assert list_of_movies == expected_movies


def test_movie_form(page: Page):
    page.goto("http://localhost:5001/movies")

    page.get_by_placeholder("Title").fill("Movie")
    page.get_by_placeholder("Release Year").fill("2000")
    page.get_by_role("button", name="Submit").click()

    expected_movies = ["Interstellar - 2009", "Inception - 2009", "Movie - 2000"]

    movies = page.locator("li")
    list_of_movies = movies.all_inner_texts()

    assert list_of_movies == expected_movies

