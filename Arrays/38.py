real_numbers = [10.5, 3.2, 15.8, 7.1, 9.0, 11.4]
given_value = 8.0

count = 0
for number in real_numbers:
    if number > given_value:
        count += 1

print("\n--- 3.20 COUNT GREATER ELEMENTS ---")
print(f"Array: {real_numbers}")
print(f"Given value: {given_value}")
print(f"Number of elements greater than {given_value}: {count}")
