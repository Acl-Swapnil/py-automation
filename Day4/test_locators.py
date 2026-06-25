from playwright.sync_api import Page

def test_locators_assignment(page: Page):
    page.goto("https://www.saucedemo.com/")

    username_field = page.get_by_placeholder("Username")
    password_field = page.get_by_placeholder("Password")
    login_button = page.get_by_role("button", name="Login")

    user_placeholder = username_field.evaluate("element => element.placeholder")
    pass_placeholder = password_field.evaluate("element => element.placeholder")
    
    print(f"\nUsername placeholder: {user_placeholder}")
    print(f"Password placeholder: {pass_placeholder}")
