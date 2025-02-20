import unittest
from src.sparse_matrix import read_sparse_matrix  # Ensure this matches your actual import path

class TestSparseMatrix(unittest.TestCase):
    def test_addition(self):
        matrix1 = SparseMatrix(3, 3, {(0, 0): 1, (0, 1): 2, (1, 1): 3, (2, 2): 4})
        matrix2 = SparseMatrix(3, 3, {(0, 0): 5, (1, 0): 6, (1, 1): 7, (2, 2): 8})
        result = matrix1 + matrix2
        expected = {(0, 0): 6, (0, 1): 2, (1, 0): 6, (1, 1): 10, (2, 2): 12}
        self.assertEqual(result.data, expected)

    def test_subtraction(self):
        matrix1 = SparseMatrix(3, 3, {(0, 0): 1, (0, 1): 2, (1, 1): 3, (2, 2): 4})
        matrix2 = SparseMatrix(3, 3, {(0, 0): 5, (1, 0): 6, (1, 1): 7, (2, 2): 8})
        result = matrix1 - matrix2
        expected = {(0, 0): -4, (0, 1): 2, (1, 0): -6, (1, 1): -4, (2, 2): -4}
        self.assertEqual(result.data, expected)

if __name__ == '__main__':
    unittest.main()
