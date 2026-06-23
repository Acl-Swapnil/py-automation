from login_module import Login
from product_module import load_products, display_products, get_product_by_id, filter_budget_items
from cart_system import Cart

def main():
    print("\nDAY 3 FINAL PROJECT - SHOPPING SYSTEM")

    auth_system = Login("Swapnil", "Swapnil@123")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    try:
        auth_system.validate_login(username, password)
        print("Login Successful\n")

        products = load_products()

        budget_items = filter_budget_items(products)
        print("Budget Items (< $50):")
        for item in budget_items:
            print(f"- {item['name']}: ${item['price']}")

        display_products(products)

        cart = Cart()

        while True:
            choice = input("\nEnter product ID to add to cart or type 'done' to checkout: ")

            if choice.lower() == "done":
                break

            try:
                product_id = int(choice)
                selected_product = get_product_by_id(products, product_id)

                if selected_product:
                    cart.add_item(selected_product)
                else:
                    print("Invalid product ID.")
            except ValueError:
                print("Please enter a valid number.")

        cart.checkout()

    except Exception as error:
        print(f"Process Terminated. Error: {error}")

if __name__ == "__main__":
    main()