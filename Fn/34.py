def f(x, y):
    total_sum = 0

    for number in range(x, y + 1):
        if (number % 2 == 0) and (number % 3 == 0) and (number % 4 != 0):
            total_sum += number

    return total_sum


print(f"f(1, 20) returns {f(1, 20)}")
print(f"f(10, 30) returns {f(10, 30)}")
print(f"f(12, 24) returns {f(12, 24)}")
