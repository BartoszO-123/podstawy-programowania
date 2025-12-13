def f(expression):
    result = int(expression[0])

    i = 1
    while i < len(expression):
        operator = expression[i]
        number = int(expression[i + 1])

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number

        i += 2

    return result


print(f'f("2+3") returns {f("2+3")}')
print(f'f("3+8+1") returns {f("3+8+1")}')
print(f'f("2+3-4+5-0") returns {f("2+3-4+5-0")}')
