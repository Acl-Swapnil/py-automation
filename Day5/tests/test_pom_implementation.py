from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_logic_moved_to_pom(page: Page):
    login_pom = LoginPage(page)
    inventory_pom = InventoryPage(page)
    checkout_pom = CheckoutPage(page)
    
    login_pom.navigate()
    login_pom.execute_login("standard_user", "secret_sauce")
    
    expect(inventory_pom.inventory_header).to_be_visible()
    assert inventory_pom.items_grid.count() >= 6
    
    inventory_pom.sort_by_price_low_to_high()
    inventory_pom.add_top_items_to_cart(2)
    inventory_pom.go_to_cart()
    
    expect(inventory_pom.cart_header).to_be_visible()
    assert inventory_pom.cart_items.count() == 2
    
    checkout_pom.start_checkout()
    checkout_pom.fill_shipping_info("Swapnil", "K", "12345")
    checkout_pom.finish_order()
    
    expect(checkout_pom.success_banner).to_be_visible()
    print("\nTest logic moved into Page Classes")
