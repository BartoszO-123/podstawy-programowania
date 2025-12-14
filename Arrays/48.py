def create_2d_arr(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


arr_3x5 = create_2d_arr(3, 5)

print("\n--- 3.30 CREATE 2D ARRAY WITH ZEROS ---")
print("3x5 Array:")
for row in arr_3x5:
    print(row)
