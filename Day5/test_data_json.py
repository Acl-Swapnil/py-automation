import json
import os
from playwright.sync_api import Page, expect
from models.login_page import LoginPage
from models.inventory_page import InventoryPage
from models.checkout_page import CheckoutPage

def test_data_driven_via_json(page: Page):
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, "data", "test_data.json")
    
    with open(json_path, "r") as file:
        test_data = json.load(file)
        
    login_pom = LoginPage(page)
    inventory_pom = InventoryPage(page)
    checkout_pom = CheckoutPage(page)
    
    login_pom.navigate()
    login_pom.execute_login(
        test_data["login"]["valid_username"], 
        test_data["login"]["password"]
    )
    
    inventory_pom.sort_by_price_low_to_high()
    inventory_pom.add_top_items_to_cart(2)
    inventory_pom.go_to_cart()
    
    checkout_pom.start_checkout()
    checkout_pom.fill_shipping_info(
        test_data["checkout"]["first_name"],
        test_data["checkout"]["last_name"],
        test_data["checkout"]["postal_code"]
    )
    checkout_pom.finish_order()
    
    expect(checkout_pom.success_banner).to_be_visible()
    print("\nFull flow run using JSON test data records")
