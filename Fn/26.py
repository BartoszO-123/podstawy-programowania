def f(palindrome):
    return palindrome == palindrome[::-1] # Check if the string is the same forwards and backwards


print(f'"radar": {f("radar")}')
print(f'"12-11-21": {f("12-11-21")}')
print(f'"book": {f("book")}')
