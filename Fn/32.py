def f(password):
  is_long_enough = len(password) >= 6
  is_unique = len(password) == len(set(password))
  return is_long_enough and is_unique

print(f'f("ax15") returns {f("ax15")}')
print(f'f("book123") returns {f("book123")}')
print(f'f("A2water3") returns {f("A2water3")}')
print(f'f("qwerty") returns {f("qwerty")}')
print(f'f("") returns {f("")}')