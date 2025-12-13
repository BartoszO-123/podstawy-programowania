# previous_price = 200.00
previous_price = int(input("Enter previous price:"))
# current_price = 140.00
current_price = int(input("Enter current price:"))
price_reduction_amount = previous_price - current_price
price_reduction_percentage = (price_reduction_amount / previous_price) * 100


recommended_threshold = 10.0

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")


if price_reduction_percentage >= recommended_threshold:
    if price_reduction_percentage == int(price_reduction_percentage):
        reduction_display = int(price_reduction_percentage)
    else:
        reduction_display = round(price_reduction_percentage, 1)

    print("\nBuy the product!!")
    print(f"Product price reduced by {reduction_display}%")
else:
    print(
        f"\nPrice reduced by {round(price_reduction_percentage, 1)}%. No purchase recommendation (required reduction: {recommended_threshold}%)"
    )
