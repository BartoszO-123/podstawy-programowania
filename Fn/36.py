def f(product_code):
    if len(product_code) != 4:
        return False

    d1 = int(product_code[0])
    d2 = int(product_code[1])
    d3 = int(product_code[2])

    checksum_digit = int(product_code[3])

    sum_of_digits = d1 + d2 + d3

    expected_checksum = sum_of_digits % 7

    return expected_checksum == checksum_digit


print(f'f("1082") returns {f("1082")}')
print(f'f("2035") returns {f("2035")}')
print(f'f("1114") returns {f("1114")}')
print(f'f("7071") returns {f("7071")}')
