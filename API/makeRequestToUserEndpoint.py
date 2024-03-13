import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = {}
if response.status_code == 200:
    users = response.json()
else:
    print("Error!!")

for user in users:
    address = user["address"]["street"] + ", " + user["address"]["suite"] + ", "  + user["address"]["city"] + ", " + user["address"]["zipcode"]
    print(f"Name: {user["name"]}\nEmail: {user["email"]}\nCompany: {user["company"]["name"]}\nAddress: {address}")