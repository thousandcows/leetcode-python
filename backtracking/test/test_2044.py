import unittest

from backtracking.n_2044_count_number_of_maximum_bitwise_or_subsets import (
    CountNumberOfMaximumBitwiseOrSubsets,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [3, 1]
        expected = 2
        self.assertEqual(
            expected, CountNumberOfMaximumBitwiseOrSubsets.solution(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [2, 2, 2]
        expected = 7
        self.assertEqual(expected, CountNumberOfMaximumBitwiseOrSubsets.solution(nums))

    def test_case_three(self):
        nums = [3, 2, 1, 5]
        expected = 6
        self.assertEqual(expected, CountNumberOfMaximumBitwiseOrSubsets.solution(nums))


if __name__ == "__main__":
    unittest.main()
