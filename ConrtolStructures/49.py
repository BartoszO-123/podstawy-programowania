try:
    number_input = input("Enter number: ")
    number = int(number_input)
except ValueError:
    print("Error: Invalid input. Please enter a whole number.")
    number = None

if number is not None:
    for i in range(1, 11):
        product = number * i
        print(f"{number} x {i} = {product}")
