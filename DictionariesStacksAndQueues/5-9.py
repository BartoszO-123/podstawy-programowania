import csv

# 1. Initialize the dictionary to store counts: {Letter: [Name, Count]}
provinces = {}

# 2. Load the province data from province.csv
# The file provides the first letter and the name of the province 
with open('province.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # We store the Name and a counter starting at 0
        provinces[row['Letter']] = {'name': row['Name'], 'count': 0}

# 3. Read the registration numbers from vehicle.txt
# Each line contains a registration number like 'ZGA5310' 
try:
    with open('vehicle.txt', 'r') as f:
        for line in f:
            registration = line.strip()
            if registration:
                # Get the first letter of the registration number 
                first_letter = registration[0]
                
                # If the letter exists in our province dictionary, increment the count
                if first_letter in provinces:
                    provinces[first_letter]['count'] += 1
except FileNotFoundError:
    print("The file vehicle.txt was not found.")

# 4. Print the results
print(f"{'Province':<25} | {'Vehicle Count'}")
print("-" * 40)
for letter, data in provinces.items():
    print(f"{data['name']:<25} | {data['count']}")