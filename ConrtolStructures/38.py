try:
    num_products = int(input("Enter the number of products purchased: "))
    if num_products < 0:
        print("Number of products reset to 0 (cannot be negative).")
        num_products = 0
except ValueError:
    print("Error: Invalid format. Number of products reset to 0.")
    num_products = 0


try:
    product_price = float(input("Enter the unit price of the product: "))
    if product_price < 0:
        print("Product price reset to 0.00 (cannot be negative).")
        product_price = 0.00
except ValueError:
    print("Error: Invalid format. Product price reset to 0.00.")
    product_price = 0.00



discount_rate = 0.25

discount_factor = 1.0 - discount_rate
amount_to_pay = 0.0

if num_products <= 2:
    amount_to_pay = num_products * product_price

else:
    num_full_price = 2
    cost_full_price = num_full_price * product_price

    num_discounted = num_products - num_full_price

    price_after_discount = product_price * discount_factor

    cost_discounted = num_discounted * price_after_discount

    amount_to_pay = cost_full_price + cost_discounted

print("\n--- Calculation Result ---")
print(f"Number of products purchased: {num_products}")
print(f"Product price: {product_price:.2f}")
print(f"Amount to pay: {amount_to_pay:.2f}")
