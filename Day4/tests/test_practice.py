from playwright.sync_api import Page, expect

def test_cart_and_checkout_practice(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    page.locator(".product_sort_container").select_option("lohi")
    page.get_by_role("button", name="Add to cart").nth(0).click()
    page.get_by_role("button", name="Add to cart").nth(0).click()
   
    page.locator(".shopping_cart_link").click()
    expect(page.get_by_text("Your Cart")).to_be_visible()
    assert page.locator(".cart_item").count() == 2

    page.get_by_role("button", name="Checkout").click()
    
    page.get_by_placeholder("First Name").fill("Swapnil")
    page.get_by_placeholder("Last Name").fill("K")
    page.get_by_placeholder("Zip/Postal Code").fill("12345")
    
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Finish").click()

    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    print("\nChecked Out successfully")