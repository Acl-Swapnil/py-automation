from day1 import login, products

print("\nSIMPLE SHOPPING SYSTEM")

user_input = input("Enter Username: ")
password_input = input("Enter Password: ")

login_status = login(user_input, password_input)

if login_status == "success":
    print("Login Sucessful")
    
    print("Adding items to your cart")
    shopping_cart = []

    shopping_cart.append(products[0])
    shopping_cart.append(products[1])
    shopping_cart.append(products[2])

    total_price = 0
    for cart_item in shopping_cart:
        print(f"- {cart_item['name']}: ${cart_item['price']}")
        total_price += cart_item['price']
        
    print(f"Total Bill: ${total_price:}")
    print("Thanks for shopping")

else:
    print("Login Failed. Invalid Credentials")
