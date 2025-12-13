def f(dice):
    if not dice:  # !dice checks for empty string
        return None

    max_length = 0
    result_digit = None

    current_digit = dice[0]
    current_length = 0

    for digit in dice:
        if digit == current_digit:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                result_digit = current_digit

            current_digit = digit
            current_length = 1

    if current_length > max_length:
        result_digit = current_digit

    return int(result_digit)


print(f'f("5233165554211") returns {f("5233165554211")}')
print(f'f("2133") returns {f("2133")}')
print(f'f("111222") returns {f("111222")}')
print(f'f("6") returns {f("6")}')
