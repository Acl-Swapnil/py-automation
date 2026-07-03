from playwright.sync_api import Page, expect
from .pages.login_page import LoginPage
from .pages.checkout_page import CheckoutPage


class TestCheckout:
    def test_full_checkout(self, page: Page, test_data):
        login = LoginPage(page)
        page.goto(test_data["base_url"])
        login.login(test_data["username"], test_data["password"])

        checkout = CheckoutPage(page)
        checkout.add_item("sauce-labs-backpack")
        expect(checkout.badge).to_have_text("1")

        checkout.go_to_cart()
        checkout.fill_form("John", "Doe", "12345")
        checkout.finish()
        expect(checkout.confirmation).to_have_text("Thank you for your order!")