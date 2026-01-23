computer_store = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

total = 0
# a list of products and the quantity
for item, quantity in computer_store.items():
    print(f'{item} : {quantity}')
# the total number of products in the store
    total += quantity

print(f'The total number of products in the store: {total}')