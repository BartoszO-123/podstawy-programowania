coins = [5, 2, 1]

try:
    amount_input = input("Enter the amount in PLN (a natural number): ")
    amount = int(amount_input)

    original_amount = amount

    if amount <= 0:
        print("Error: The amount must be a natural number (a positive integer).")

        amount = -1

except ValueError:
    print("Error: Invalid input. Please enter a whole number.")
    amount = -1


if amount > 0:
    count_5_pln = 0
    count_2_pln = 0
    count_1_pln = 0

    remaining_amount = amount

    count_5_pln = remaining_amount // 5

    remaining_amount = remaining_amount % 5

    count_2_pln = remaining_amount // 2
    remaining_amount = remaining_amount % 2

    count_1_pln = remaining_amount

    print(f"\nThe amount of PLN {original_amount} in coins:")
    print(f"5 PLN coins: {count_5_pln}")
    print(f"2 PLN coins: {count_2_pln}")
    print(f"1 PLN coins: {count_1_pln}")
