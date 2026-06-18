import requests

url = "https://github.com"

try:
    response = requests.get(url, timeout=5)
    api_data = response.json()
    print(f"Status: {response.status_code} - Content Parsed Successfully")
except Exception:
    print("Network down. Using local data.")
    api_data = {
        "id": 5832347,
        "name": "Swapnil K"
    }

print(f"User ID: {api_data.get('id')}")
print(f"Name: {api_data.get('name')}")