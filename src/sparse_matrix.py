import os

class SparseMatrix:
    """A class to represent a sparse matrix using a dictionary."""

    def __init__(self, rows, cols, values=None):
        self.rows = rows
        self.cols = cols
        self.values = values if values else {}  # Dictionary {(row, col): value}

    def add(self, other):
        """Adds two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix addition not possible: Incompatible dimensions.")
        return SparseMatrix(self.rows, self.cols, add_matrices(self.values, other.values))

    def subtract(self, other):
        """Subtracts two sparse matrices."""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix subtraction not possible: Incompatible dimensions.")
        return SparseMatrix(self.rows, self.cols, subtract_matrices(self.values, other.values))

    def multiply(self, other):
        """Multiplies two sparse matrices."""
        if self.cols != other.rows:
            raise ValueError("Matrix multiplication not possible: Incompatible dimensions.")
        return SparseMatrix(self.rows, other.cols, multiply_matrices(self.values, other.values, self.rows, self.cols, other.cols))

    def __repr__(self):
        return f"SparseMatrix({self.rows}, {self.cols}, {self.values})"

    @classmethod
    def from_file(cls, filename):
        """Reads a sparse matrix from a file."""
        file_path = os.path.join(os.path.dirname(__file__), "../sample_inputs", filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Error: File '{filename}' not found at {file_path}")

        with open(file_path, "r") as file:
            lines = file.readlines()

        if len(lines) < 2:
            raise ValueError("Invalid file format: Missing row/column info.")

        try:
            rows = int(lines[0].split('=')[1])  # Extract number of rows
            cols = int(lines[1].split('=')[1])  # Extract number of columns
            values = {}
            for line in lines[2:]:  # Read matrix data
                row, col, value = map(int, line.strip('()\n').split(','))
                values[(row, col)] = value
        except (ValueError, IndexError):
            raise ValueError("Invalid file format: Unable to parse matrix data.")

        return cls(rows, cols, values)

    def to_file(self, filename):
        """Writes the sparse matrix to a file."""
        with open(filename, 'w') as file:
            file.write(f"rows={self.rows}\ncols={self.cols}\n")
            for (row, col), value in sorted(self.values.items()):
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
    """Multiplies two sparse matrices if dimensions are valid."""
    result = {}
    for (row1, col1), value1 in matrix1.items():
        for (row2, col2), value2 in matrix2.items():
            if col1 == row2:  # Valid multiplication condition
                result[(row1, col2)] = result.get((row1, col2), 0) + (value1 * value2)
    return result

# Main Execution
if __name__ == "__main__":
    try:
        # Read input matrices
        matrix1 = SparseMatrix.from_file("matrix1.txt")
        matrix2 = SparseMatrix.from_file("matrix2.txt")

        # Perform matrix operations
        added_matrix = matrix1.add(matrix2)
        subtracted_matrix = matrix1.subtract(matrix2)
        multiplied_matrix = matrix1.multiply(matrix2)

        # Write results to output files
        added_matrix.to_file("output_add.txt")
        subtracted_matrix.to_file("output_subtract.txt")
        multiplied_matrix.to_file("output_multiply.txt")

        print("Matrix operations completed successfully. Results saved to files.")
    except Exception as e:
        print(f"Error: {e}")

