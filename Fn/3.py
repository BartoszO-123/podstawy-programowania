###
# Calculates the sum of the digits in a number
#


def sum_digits(number):
    abs_number = abs(number)  # --- przerobienie na wartość bezwzględną ---

    num_str = str(abs_number)  # --- przerobienie na string ---

    digit_sum = 0
    for digit_char in num_str:
        digit_sum += int(digit_char)

    return digit_sum


any_number = int(input("Enter integer number: "))


result = sum_digits(any_number)


print(f"The sum of the digits in the number {any_number} is {result}")
