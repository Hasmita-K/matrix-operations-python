# Matrix Operations Mini Project

def add_matrices(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] 
              for i in range(len(A))]
    return result


def subtract_matrices(A, B):
    result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] 
              for i in range(len(A))]
    return result


def multiply_matrices(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def display_matrix(matrix):
    for row in matrix:
        print(row)


# Sample matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [1, 2, 3]
]

C = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print("Matrix A:")
display_matrix(A)

print("\nMatrix B:")
display_matrix(B)

print("\nAddition (A + B):")
display_matrix(add_matrices(A, B))

print("\nSubtraction (A - B):")
display_matrix(subtract_matrices(A, B))

print("\nMultiplication (A x C):")
display_matrix(multiply_matrices(A, C))

print("\nTranspose of A:")
display_matrix(transpose_matrix(A))