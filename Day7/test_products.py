from playwright.sync_api import Page, expect


class TestProducts:
    def test_products_count(self, page: Page, test_data):
        page.goto(test_data["base_url"])
        page.fill("#user-name", test_data["username"])
        page.fill("#password", test_data["password"])
        page.click("#login-button")
        items = page.locator(".inventory_item")
        expect(items).to_have_count(6)

    def test_add_to_cart(self, page: Page, test_data):
        page.goto(test_data["base_url"])
        page.fill("#user-name", test_data["username"])
        page.fill("#password", test_data["password"])
        page.click("#login-button")
        page.click("#add-to-cart-sauce-labs-backpack")
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")