matrix = [[7, 3, 7, 9, 0], [2, 9, 0, 1, 5], [3, 8, 6, 4, 7], [8, 7, 1, 1, 5]]

last_column_sum = 0
last_col_index = len(matrix[0]) - 1

for row in matrix:
    last_column_sum += row[last_col_index]

print("\n--- 3.29 SUM OF LAST COLUMN ---")
print(f"Matrix: {matrix}")
print(f"Sum of values in the last column: {last_column_sum}")
