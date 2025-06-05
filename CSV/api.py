import requests
import csv

response= requests.get("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv")
data=response.content

with open("output_dict.csv", mode="w", newline="", encoding="utf-8") as file:
    csv.writer.writerows(data)