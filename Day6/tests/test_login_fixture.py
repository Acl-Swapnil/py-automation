from pages.login_page import LoginPage

def test_login_success(logged_in_page):
    assert "inventory.html" in logged_in_page.url
    assert logged_in_page.locator(".title").inner_text() == "Products"


def test_inventory_page_has_items(logged_in_page):
    items = logged_in_page.locator(".inventory_item")
    assert items.count() >= 6


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("invalid_user", "wrong_pass")
    assert login_page.error_message.is_visible()