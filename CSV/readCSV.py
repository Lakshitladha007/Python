import csv
import requests
from io import StringIO
import json

response=requests.get("https://jsonplaceholder.typicode.com/users")

data=json.loads(response.text)
print(data)

with open("users.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ID", "Name", "Username", "Email", "City"])
    
    for user in data:
        writer.writerow([
            user["id"],
            user["name"],
            user["username"],
            user["email"],
            user["address"]["city"]
        ])

print("CSV file 'users.csv' written successfully.")