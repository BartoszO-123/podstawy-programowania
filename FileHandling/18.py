import csv


with open("it_company.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)  # czytnik csv

    for row in reader:
        print(f"{row[0]} {row[1]},{row[3]}")
