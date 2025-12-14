arr = [15, 8, 31, 47, 2, 19]
total_sum = 0

for num in arr:
    total_sum += num

arithmetic_mean = total_sum / len(arr)

print("\n--- 3.6 ARITHMETIC MEAN (FOR) ---")
print(f"Array: {arr}")
print(f"Arithmetic mean: {arithmetic_mean:.2f}")