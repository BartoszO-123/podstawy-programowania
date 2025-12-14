product_prices = [
    2999.99,
    149.99,
    499.99,
    89.99,
    1199.99,
    349.99,
    189.99,
    99.99,
    249.99,
    999.99,
]
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

total_value = 0
for price, quantity in zip(product_prices, product_quantities):
    total_value += price * quantity

print("\nTotal value of goods in the store:")
print(f"Total value: {total_value:.2f}")
