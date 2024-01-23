import unittest

from graphs.n_78_subsets import Subsets
from utils.helper_functions import HelperFunctions


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 2, 3]
        expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        result = Subsets.solution(nums)
        self.assertEqual(
            True, HelperFunctions.compare_two_dimensional_arrays(expected, result)
        )  # add assertion here

    def test_case_two(self):
        nums = [0]
        expected = [[], [0]]
        result = Subsets.solution(nums)
        self.assertEqual(
            True, HelperFunctions.compare_two_dimensional_arrays(expected, result)
        )


if __name__ == "__main__":
    unittest.main()
