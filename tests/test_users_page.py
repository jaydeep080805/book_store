from playwright.sync_api import Page, expect
from lib.user import User
from lib.user_repository import UserRepository

def test_users_page_has_title(page: Page):
    Page.goto(page, "http://localhost:5001/users")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Users")

def test_list_of_users_is_empty_with_inital_seed(page: Page):
    Page.goto(page, "http://localhost:5001/users")

    list_of_users = page.locator("li")

    assert list_of_users.all_text_contents() == []

def test_user_form_adds_to_database(page: Page, db):
    user_repo = UserRepository(db)
    
    Page.goto(page, "http://localhost:5001/sign-up")

    page.get_by_placeholder("Username").fill("test_username_form")
    page.get_by_placeholder("Password").fill("test_password_form")

    page.get_by_role("button").click()

    new_user = User(1, "test_username_form", "test_password_form")

    all_users = user_repo.all()

    assert len(all_users) == 1
    assert all_users[0] == new_user