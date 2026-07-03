from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage


class TestLogin:
    def test_valid_login(self, page: Page, test_data):
        login = LoginPage(page)
        page.goto(test_data["base_url"])
        login.login(test_data["username"], test_data["password"])
        expect(page.locator(".title")).to_have_text("Products")

    def test_invalid_login(self, page: Page, test_data):
        login = LoginPage(page)
        page.goto(test_data["base_url"])
        login.login("wrong_user", "wrong_pass")
        expect(login.error).to_be_visible()
        assert "Epic sadface" in login.get_error()

    def test_locked_user(self, page: Page, test_data):
        login = LoginPage(page)
        page.goto(test_data["base_url"])
        login.login(test_data["locked_user"], test_data["password"])
        assert "locked out" in login.get_error()