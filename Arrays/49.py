multiplication_table = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

n = len(multiplication_table)

for i in range(n):
    for j in range(n):
        multiplication_table[i][j] = (i + 1) * (j + 1)

print("\n--- 3.31 MULTIPLICATION TABLE ---")
for row in multiplication_table:
    print(" ".join(f"{x:2}" for x in row))
