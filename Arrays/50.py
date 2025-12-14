arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_val, min_r, min_c = arr[0][0], 0, 0
max_val, max_r, max_c = arr[0][0], 0, 0

for r_idx, row in enumerate(arr):
    for c_idx, val in enumerate(row):
        if val < min_val:
            min_val, min_r, min_c = val, r_idx, c_idx
        if val > max_val:
            max_val, max_r, max_c = val, r_idx, c_idx

print("\n--- 3.32 FIND MIN/MAX IN 2D ARRAY ---")
print(f"Array: {arr}")
print(f"Smallest value: {min_val} (Row {min_r + 1}, Column {min_c + 1})")
print(f"Largest value: {max_val} (Row {max_r + 1}, Column {max_c + 1})")
