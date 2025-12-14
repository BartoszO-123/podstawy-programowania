matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

n = len(matrix)

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1

print("\nMatrix with ones on the main diagonal:")
for row in matrix:
    print(" ".join(map(str, row)))
