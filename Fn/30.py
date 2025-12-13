def f(number1, number2, number3):
    numbers = [number1, number2, number3]
    max_number = max(numbers)
    min_number = min(numbers)
    return max_number - min_number


print(f"f(7, 4, 9) returns {f(7, 4, 9)}")
print(f"f(2, 12, 8) returns {f(2, 12, 8)}")
print(f"f(10, 10, 10) returns {f(10, 10, 10)}")
