import unittest

from simulation.n_54_spiral_matrix import SpiralMatrix


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(expected, SpiralMatrix.solution(matrix))  # add assertion here

    def test_case_two(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(expected, SpiralMatrix.solution(matrix))

    def test_case_three(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(expected, SpiralMatrix.solution(matrix))


if __name__ == "__main__":
    unittest.main()
