import numpy as np

def rotate(matrix: list):
    """
    Rotate a matrix 90 degrees clockwise in-place
    :param matrix: list[list[int]]
    :return: list[list[int]]

    In case you want to reinvent the wheel:
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    return matrix
    """
    return np.rot90(matrix, k=3).tolist()

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]))