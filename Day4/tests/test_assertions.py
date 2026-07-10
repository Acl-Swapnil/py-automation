from playwright.sync_api import Page, expect

def test_assertions_assignment(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_title("Swag Labs")

    inventory_header = page.get_by_text("Products")
    expect(inventory_header).to_be_visible()

    products = page.locator(".inventory_item")
    actual_count = products.count()
    
    assert actual_count >= 6
    print(f"\nVerified: {actual_count} items found")