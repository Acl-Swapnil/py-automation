import json

def load_products():
    try:
        with open("products.json", "r") as file:
            products = json.load(file)
            return products
    except Exception:
        print("products.json file not found.")

def display_products(products):
    print("\nAvailable Products:")
    for product in products:
        print(f"{product['id']}. {product['name']} - ${product['price']}")

def get_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def filter_budget_items(products):
    return [product for product in products if product["price"] < 50]