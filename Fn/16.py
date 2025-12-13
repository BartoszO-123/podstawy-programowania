import binary_checker

# Testowanie poprawnych i niepoprawnych wartości
print(f'f("101101") returns {binary_checker.f("101101")}')
print(f'f("1311a10100") returns {binary_checker.f("1311a10100")}')
print(f'f("110111") returns {binary_checker.f("110111")}')
