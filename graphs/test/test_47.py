import unittest

from graphs.n_47_permutations_two import PermutationsTwo
from utils.helper_functions import HelperFunctions


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 1, 2]
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        self.assertEqual(
            True,
            HelperFunctions.compare_two_dimensional_arrays(
                expected, PermutationsTwo.solution(nums)
            ),
        )  # add assertion here

    def test_case_two(self):
        nums = [1, 2, 3]
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(
            True,
            HelperFunctions.compare_two_dimensional_arrays(
                expected, PermutationsTwo.solution(nums)
            ),
        )

    def test_case_three(self):
        nums = [0, 1]
        expected = [[0, 1], [1, 0]]
        self.assertEqual(
            True,
            HelperFunctions.compare_two_dimensional_arrays(
                expected, PermutationsTwo.solution(nums)
            ),
        )

    def test_case_four(self):
        nums = [1]
        expected = [[1]]
        self.assertEqual(
            True,
            HelperFunctions.compare_two_dimensional_arrays(
                expected, PermutationsTwo.solution(nums)
            ),
        )


if __name__ == "__main__":
    unittest.main()
