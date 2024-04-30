def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    return [list(row) for row in zip(*matrix)]

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix1))