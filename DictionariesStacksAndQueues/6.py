price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

# prints a list of products and their prices before the discount
total = 0
for product, price in price_list.items():
    print(f'{product} : {price}')
    
# prints the total value of the products before the discount
    total += price
print(f'\nthe total value of the products before the discount: {total:.2f}\n')

# modifies the price list according to the discount (round prices to two decimal places)
for product in price_list:
    discount = price_list[product] * 0.90
    price_list[product] = round(discount, 2)
    
# prints a list of products and their prices after the 10% discount
total_after = 0
for product, price in price_list.items():
    print(f'{product} : {price}')
    
# prints the total value of the products after the discount
    total_after += price
print(f'\nthe total value of the products after the discount: {total:.2f}')
