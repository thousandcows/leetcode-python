import unittest

from mathmatics.n_1979_find_greatest_common_divisor_of_array import (
    FindGreatestCommonDivisorOfArray,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [2, 6, 8, 14]
        expected = 2
        self.assertEqual(
            expected, FindGreatestCommonDivisorOfArray.solution(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [3, 6, 9]
        expected = 3
        self.assertEqual(expected, FindGreatestCommonDivisorOfArray.solution(nums))

    def test_case_three(self):
        nums = [7, 5, 6, 8, 3]
        expected = 1
        self.assertEqual(expected, FindGreatestCommonDivisorOfArray.solution(nums))


if __name__ == "__main__":
    unittest.main()
