arr = [15, 8, 31, 47, 2, 19]
total_sum = 0
n = len(arr)

for num in arr:
    total_sum += num

arithmetic_mean = total_sum / n

print("\n--- 3.7 ARITHMETIC MEAN (WHILE) ---")
print(f"Array: {arr}")
print(f"Arithmetic mean: {arithmetic_mean:.2f}")
