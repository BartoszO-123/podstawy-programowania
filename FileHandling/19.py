import csv

file_name = "clothing.csv"

print("PRODUCTS WITH LOW STOCK AND LOW PRICE")
print("========================================")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # pomijam nagłówek

        for row in reader:
            name = row[1]
            price = float(row[5])
            quantity = int(row[6])

            if price < 60 and quantity < 40:
                print(f"Product: {name}, Price: {price}, Stock: {quantity}")

except FileNotFoundError:
    print("File clothing.csv not found")
