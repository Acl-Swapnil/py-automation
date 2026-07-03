from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_btn = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.confirmation = page.locator(".complete-header")

    def add_item(self, item_id: str):
        self.page.click(f"#add-to-cart-{item_id}")

    def go_to_cart(self):
        self.cart_link.click()

    def fill_form(self, first: str, last: str, postal: str):
        self.checkout_btn.click()
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal.fill(postal)
        self.continue_btn.click()

    def finish(self):
        self.finish_btn.click()