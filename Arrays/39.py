arr = [7, 9, 2, 4, 5, 6]
even_numbers = []
odd_numbers = []

for num in arr:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

arr_separated = even_numbers + odd_numbers

print("\n--- 3.21 SEPARATE EVEN AND ODD ---")
print(f"Original array: {arr}")
print(f"Separated array: {arr_separated}")
