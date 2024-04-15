import unittest

from simulation.n_2482_difference_between_ones_and_zeroes_in_row_and_column import (
    DifferenceBetweenOnesAndZerosInRowAndColumn,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]
        expected = [[0, 0, 4], [0, 0, 4], [-2, -2, 2]]
        self.assertEqual(
            expected, DifferenceBetweenOnesAndZerosInRowAndColumn.solution(grid)
        )  # add assertion here

    def test_case_two(self):
        grid = [[1, 1, 1], [1, 1, 1]]
        expected = [[5, 5, 5], [5, 5, 5]]
        self.assertEqual(
            expected, DifferenceBetweenOnesAndZerosInRowAndColumn.solution(grid)
        )


if __name__ == "__main__":
    unittest.main()
