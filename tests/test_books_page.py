from playwright.sync_api import Page, expect
import pytest

def test_has_title(page: Page):
    Page.goto(page, url="http://127.0.0.1:5001/books")

    h1 = Page.locator(page, "h1")

    expect(h1).to_have_text("Books")


def test_list_of_books_is_correct(page: Page, db):
    # my solution
    # Page.goto(page, url="http://127.0.0.1:5001/books")

    # list_of_books = Page.locator(page, "li").all()

    # # print(list_of_books[0].all_text_contents())

    # book_titles = [['The Gruffalo by Julia Donaldson'], ['Ada Twist, Scientist by Andrea Beaty'], ['The Girl Who Drank the Moon by Kelly Barnhill'], ['Dragons in a Bag by Zetta Elliott']]

    # for index, book in enumerate(list_of_books):
    #     expect(book).to_contain_text(book_titles[index])
        

    # expect().to_contain_text(['The Gruffalo by Julia Donaldson', 'Ada Twist, Scientist by Andrea Beaty', 'The Girl Who Drank the Moon by Kelly Barnhill', 'Dragons in a Bag by Zetta Elliott'])
    # assert len(list_of_books) == 4


    # example solution

    page.goto("http://127.0.0.1:5001/books")

    books = page.locator('li')

    expected_books = [
        'The Gruffalo by Julia Donaldson',
        'Ada Twist, Scientist by Andrea Beaty',
        'The Girl Who Drank the Moon by Kelly Barnhill',
        'Dragons in a Bag by Zetta Elliott',
        'The Brain by New Scientist'
    ]

    # here's the neat part which saves you from iterating over the `li` elements
    actual_books = books.all_inner_texts()

    assert actual_books == expected_books

def test_create_books_inserts_book_into_database(page: Page):
    # create new user
    page.goto("http://localhost:5001/sign-up")
    page.get_by_placeholder("Username").fill("test_user")
    page.get_by_placeholder("password").fill("test_password")
    page.get_by_role("button", name="Submit").click()
    

    # login
    page.goto("http://localhost:5001/login")
    page.get_by_placeholder("Username").fill("test_user")
    page.get_by_placeholder("password").fill("test_password")
    page.get_by_role("button", name="Submit").click()

    # print(page.content())
    # page.wait_for_load_state("domcontentloaded")
    # page.wait_for_url("http://localhost:5001/books")

    # add the new book
    # print(f'>>> placeholder: {page.get_by_placeholder("Title")}')
    
    # insert the boko info
    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")
    page.get_by_role("button", name="Submit").click()

    # print(f">>> HEADING: {page.locator('h1').all_inner_texts()}")

    books = page.locator("li")

    # print(f">>> {books}")
    new_book = books.all_inner_texts()[-1]

    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"
