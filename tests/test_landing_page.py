from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    Page.goto(page, url="http://127.0.0.1:5001/")

    h1 = Page.locator(page, "h1")

    expect(h1).to_have_text("Welcome to the book store")

