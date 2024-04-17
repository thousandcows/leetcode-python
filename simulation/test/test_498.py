import unittest

from simulation.n_498_diagonal_traverse import DiagonalTraverse


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
        self.assertEqual(expected, DiagonalTraverse.solution(mat))  # add assertion here

    def test_case_two(self):
        mat = [[1, 2], [3, 4]]
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, DiagonalTraverse.solution(mat))

    def test_case_three(self):
        mat = [[2, 3]]
        expected = [2, 3]
        self.assertEqual(expected, DiagonalTraverse.solution(mat))


if __name__ == "__main__":
    unittest.main()
