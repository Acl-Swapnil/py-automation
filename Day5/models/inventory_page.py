from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_header = page.get_by_text("Products")
        self.items_grid = page.locator(".inventory_item")
        self.sort_select = page.locator(".product_sort_container")
        self.add_to_cart_btn = page.get_by_role("button", name="Add to cart")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_header = page.get_by_text("Your Cart")
        self.cart_items = page.locator(".cart_item")

    def sort_by_price_low_to_high(self):
        self.sort_select.select_option("lohi")

    def add_top_items_to_cart(self, quantity: int):
        for _ in range(quantity):
            self.add_to_cart_btn.nth(0).click()

    def go_to_cart(self):
        self.cart_link.click()
