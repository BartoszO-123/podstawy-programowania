arr_3x5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
print("\n--- 3.33 SWAP FIRST AND LAST ROW ---")
print("Before swap:")
for row in arr_3x5:
    print(row)

arr_3x5[0], arr_3x5[-1] = arr_3x5[-1], arr_3x5[0]

print("\nAfter swap:")
for row in arr_3x5:
    print(row)
