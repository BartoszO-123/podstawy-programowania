from collections import Counter #


def f(number):
    s_number = str(number)

    counts = Counter(s_number)

    total_sum = 0

    for digit_char, count in counts.items():
        if count > 1:
            digit_int = int(digit_char)

            total_sum += digit_int * count

    return total_sum


print(f"f(1027) returns {f(1027)}")


print(f"f(230335) returns {f(230335)}")


print(f"f(513553007) returns {f(513553007)}")
