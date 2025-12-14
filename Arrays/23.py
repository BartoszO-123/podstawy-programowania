arr = [-15, 8, -31, 47, -2, 19]

min_num = arr[0]
max_num = arr[0]

for num in arr[1:]:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("\n--- 3.5 MIN AND MAX ---")
print(f"Array: {arr}")
print(f"Minimum number: {min_num}")
print(f"Maximum number: {max_num}")
