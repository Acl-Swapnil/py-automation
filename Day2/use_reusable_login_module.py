from reusable_login_module import Login

auth_system = Login("Swapnil", "Swapnil@123")

user_input = input("Enter username: ")
password_input = input("Enter password: ")

result = auth_system.validate_login(user_input, password_input)
print(f"Login Result: {result}")
