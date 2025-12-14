def transpose_matrix(m):
    if not m or not m[0]:
        return []

    rows = len(m)
    cols = len(m[0])

    transposed = [[0] * rows for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            transposed[c][r] = m[r][c]

    return transposed


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
matrix_c = [[5, 6, 7, 8]]

print("\n--- 3.36 TRANSPOSE MATRIX ---")

print("1. Matrix A Transpose:")
transposed_a = transpose_matrix(matrix_a)
print_matrix(transposed_a)

print("2. Matrix B Transpose:")
transposed_b = transpose_matrix(matrix_b)
print_matrix(transposed_b)

print("3. Matrix C Transpose:")
transposed_c = transpose_matrix(matrix_c)
print_matrix(transposed_c)
