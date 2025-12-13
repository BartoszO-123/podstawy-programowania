try:
    decimal_number = int(input("Enter a decimal number: "))

    original_number = decimal_number

except ValueError:
    print("Error: The entered value is not a valid integer.")

    decimal_number = -1
    original_number = None


binary_number = ""


if decimal_number >= 0:
    if decimal_number == 0:
        binary_number = "0"

    else:
        while decimal_number > 0:
            remainder = decimal_number % 2

            binary_number = str(remainder) + binary_number

            decimal_number = decimal_number // 2

    if original_number is not None:
        print(f"{original_number}(10) = {binary_number}(2)")


elif decimal_number < 0:
    print("Error: The program only supports non-negative numbers.")
