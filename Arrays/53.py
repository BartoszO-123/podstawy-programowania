def identity_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix


def print_2d_array(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print("-" * 15)


print("\n--- 3.35 IDENTITY MATRICES ---")

print("Identity Matrix (3x3):")
print_2d_array(identity_matrix(3))

print("Identity Matrix (5x5):")
print_2d_array(identity_matrix(5))

print("Identity Matrix (8x8):")
print_2d_array(identity_matrix(8))
