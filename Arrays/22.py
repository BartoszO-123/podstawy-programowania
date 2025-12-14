arr = [8, 2, 5, 1, 9]
second_power = []

for num in arr:
    second_power.append(num ** 2)

print("\n--- 3.4 SECOND POWER ---")
print(f"Array: {' '.join(map(str, arr))}")
print(f"2nd power: {' '.join(map(str, second_power))}")