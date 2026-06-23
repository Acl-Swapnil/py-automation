class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"{product['name']} added to cart.")

    def view_cart(self):
        if not self.items:
            print("\nYour cart is empty.")
            return 0

        total_price = 0
        print("\nYour Cart:")
        for item in self.items:
            print(f"- {item['name']} : ${item['price']}")
            total_price += item["price"]

        print(f"Total Price: ${total_price}")
        return total_price

    def checkout(self):
        if not self.items:
            print("Cannot checkout. Cart is empty.")
            return

        total_price = self.view_cart()
        print("\nCheckout Successful")
        print(f"Final Bill: ${total_price}")
        print("Thanks for shopping")