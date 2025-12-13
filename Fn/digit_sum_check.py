def f(number, even):
    s = str(number)
    total_sum = 0
    
    for digit_char in s:
        digit = int(digit_char)
        is_digit_even = (digit % 2 == 0)
        
        if even == is_digit_even:
            total_sum += digit
            
    return total_sum