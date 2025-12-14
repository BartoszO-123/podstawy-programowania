integer_numbers = [34, 7, 19, 4, 21, 8]
even_count = 0

for num in integer_numbers:
    if num % 2 == 0:
        even_count += 1

print("\n--- 3.2 EVEN COUNT ---")
print(f"Array: {integer_numbers}")
print(f"Number of even values: {even_count}")
