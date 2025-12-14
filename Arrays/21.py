natural_numbers = [15, 8, 31, 47, 2, 19]

print("\n--- 3.3 REVERSE ARRAY ---")
print(f"Existed array: {' '.join(map(str, natural_numbers))}")

reverse_array = []
for i in range(len(natural_numbers) - 1, -1, -1):
    reverse_array.append(natural_numbers[i])

print(f"Reverse array: {' '.join(map(str, reverse_array))}")
