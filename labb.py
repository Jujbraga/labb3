import csv

with open("supportarenden.csv", newline="", encoding="utf-8" ) as file:
    reader = csv.reader(file)
    data = list(reader)

print(data)