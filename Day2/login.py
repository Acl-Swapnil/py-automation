import json

name = "Swapnil"
age = "25"
is_indian = True

print(f"Name: {name}, Age: {age}, Indian Nationality: {is_indian}")

MY_USERNAME = "Swapnil"
MY_PASSWORD = "Swapnil@123"

with open("products.json", "r") as file:
    products = json.load(file)

def login(username, password):
    if username == MY_USERNAME and password == MY_PASSWORD:
        return "success"
    else:
        raise Exception("Invalid Credentials")

for item in products:
    print(f"ID: {item['id']} | Product: {item['name']} | Price: {item['price']}")
