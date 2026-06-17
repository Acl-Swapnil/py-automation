name="Swapnil"
age="25"
is_indian = True

print(f"Name: {name}, Age: {age}, Indian Nationality: {is_indian}")

MY_USERNAME = "Swapnil"
MY_PASSWORD = "Swapnil@123"

products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Keyboard", "price": 49}
]

def login(username, password):
    if username == MY_USERNAME and password == MY_PASSWORD:
        return "success"
    else:
        return "failure"


for item in products:
    print(f"ID: {item['id']} | Product: {item['name']} | Price: {item['price']}")




