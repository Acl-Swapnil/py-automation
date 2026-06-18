import json
import requests

class Login:
    def __init__(self, correct_username, correct_password):
        self.correct_username = correct_username
        self.correct_password = correct_password

    def validate_login(self, username, password):
        if username == self.correct_username and password == self.correct_password:
            return True
        else:
            raise Exception("Invalid Credentials")

print("\n DAY 2 FINAL")

auth_system = Login("Swapnil", "Swapnil@123")
user_input = input("Enter Username: ")
password_input = input("Enter Password: ")

try:
    auth_system.validate_login(user_input, password_input)
    print("Login Verified Successfully.\n")
    
    with open("products.json", "r") as file:
        all_products = json.load(file)
        
    cheap_items = [p for p in all_products if p["price"] < 50]
    
    print("Available Budget Items (< $50):")
    for item in cheap_items:
        print(f"- {item['name']}: ${item['price']}")
        
    url = "https://github.com"
    try:
        response = requests.get(url, timeout=5)
        api_data = response.json()
        print("System Status: Online")
    except Exception:
        print("System Status: Offline")

except Exception as error:
    print(f"Process Terminated. Error: {error}")
