# matrix_operations.py
def read_sparse_matrix(filename):
    """Reads a sparse matrix from a file and returns it as a dictionary."""
    matrix = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        rows = int(lines[0].split('=')[1])  
        cols = int(lines[1].split('=')[1])  

        for line in lines[2:]:  
            row, col, value = map(int, line.strip('()\n').split(','))
            matrix[(row, col)] = value

    return matrix, rows, cols

def write_sparse_matrix(filename, matrix, rows, cols):
    """Writes a sparse matrix dictionary to a file in the correct format."""
    with open(filename, 'w') as file:
        file.write(f"rows={rows}\n")
        file.write(f"cols={cols}\n")
        for (row, col), value in sorted(matrix.items()):
            file.write(f"({row},{col},{value})\n")

def add_matrices(matrix1, matrix2):
    """Adds two sparse matrices."""
    result = matrix1.copy()
    for key, value in matrix2.items():
        result[key] = result.get(key, 0) + value
    return result

def subtract_matrices(matrix1, matrix2):
    """Subtracts two sparse matrices."""
    result = matrix1.copy()
    for key, value in matrix2.items():
        result[key] = result.get(key, 0) - value
    return result

def multiply_matrices(matrix1, matrix2, rows1, cols1, cols2):
    """Multiplies two sparse matrices."""
    result = {}

    for (row1, col1), value1 in matrix1.items():
        for (row2, col2), value2 in matrix2.items():
            if col1 == row2:  
                result[(row1, col2)] = result.get((row1, col2), 0) + (value1 * value2)

    return result

