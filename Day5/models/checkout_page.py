from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_btn = page.get_by_role("button", name="Checkout")
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_btn = page.get_by_role("button", name="Continue")
        self.finish_btn = page.get_by_role("button", name="Finish")
        self.success_banner = page.get_by_text("Thank you for your order!")

    def start_checkout(self):
        self.checkout_btn.click()

    def fill_shipping_info(self, first_name, last_name, zip_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(zip_code)
        self.continue_btn.click()

    def finish_order(self):
        self.finish_btn.click()
