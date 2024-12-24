import numpy as np


def process_matrix(matrix):
    # Extract the second column
    second_column = matrix[:, 1]

    # Extract the last row
    last_row = matrix[-1, :]

    # Reshape the matrix into a 1D array
    reshaped_matrix = matrix.reshape(-1)

    # Transpose the matrix
    transposed_matrix = matrix.T

    return second_column, last_row, reshaped_matrix, transposed_matrix


# Example usage
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

second_column, last_row, reshaped_matrix, transposed_matrix = process_matrix(matrix)

print("Second column:", second_column)
print("Last row:", last_row)
print("Reshaped matrix:", reshaped_matrix)
print("Transposed matrix:\n", transposed_matrix)
