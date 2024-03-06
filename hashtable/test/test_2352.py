import unittest

from hashtable.n_2352_equal_row_and_column_pairs import EqualRowAndColumnPairs


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        expected = 1
        self.assertEqual(
            expected, EqualRowAndColumnPairs.solution_two(grid)
        )  # add assertion here

    def test_case_two(self):
        grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
        expected = 3
        self.assertEqual(expected, EqualRowAndColumnPairs.solution_two(grid))


if __name__ == "__main__":
    unittest.main()
