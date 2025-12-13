import math


def is_prime(num):
    if num <= 1:
        return False

    for i in range(
        2, int(math.sqrt(num)) + 1
    ):  # Sprawdź dzielniki
        if num % i == 0:
            return False

    return True


def f(n):
    if n <= 0:
        return "Wymagane n > 0"

    count = 0
    num = 1

    while count < n:
        num += 1
        if is_prime(num):
            count += 1

    return num


print(f"f(1) returns {f(1)}")


print(f"f(5) returns {f(5)}")


print(f"f(10) returns {f(10)}")
