arr_3x5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
cols = len(arr_3x5[0])
first_col_idx = 0
last_col_idx = cols - 1

print("\n--- 3.34 SWAP FIRST AND LAST COLUMN ---")
print("Before swap:")
for row in arr_3x5:
    print(row)

for row in arr_3x5:
    row[first_col_idx], row[last_col_idx] = row[last_col_idx], row[first_col_idx]

print("\nAfter swap:")
for row in arr_3x5:
    print(row)
