from playwright.sync_api import Page, expect
from lib.users.user import User
from lib.users.user_repository import UserRepository

def test_users_page_has_title(page: Page):
    Page.goto(page, "http://localhost:5001/users")

    h1 = page.locator("h1")

    expect(h1).to_have_text("Users")

def test_list_of_users_is_empty_with_inital_seed(page: Page, db):
    # needs reseeding since the books page now needs to create a user
    db.seed("seeds/users.sql")
    
    Page.goto(page, "http://localhost:5001/users")

    list_of_users = page.locator("li")

    assert list_of_users.all_text_contents() == []

def test_user_form_adds_to_database(page: Page, db, bcrypt):
    user_repo = UserRepository(db, bcrypt)
    
    Page.goto(page, "http://localhost:5001/sign-up")

    page.get_by_placeholder("Username").fill("test_username_form")
    page.get_by_placeholder("Password").fill("test_password_form")

    page.get_by_role("button").click()
    
    all_users = user_repo.all()

    assert len(all_users) == 1
    assert all_users[-1].username == "test_username_form"
    assert bcrypt.check_password_hash(all_users[-1].password, "test_password_form")