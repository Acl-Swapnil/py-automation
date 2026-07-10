from playwright.sync_api import Page

def test_login_scenarios(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    
    page.get_by_role("button", name="Login").click()

    error_message = page.get_by_text("Epic sadface")
    if error_message.is_visible():
        print("\nError Scenario: Successfully tested")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    inventory_header = page.get_by_text("Products")
    if inventory_header.is_visible():
        print("Success Scenario: Successfully tested")