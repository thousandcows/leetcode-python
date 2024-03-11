import unittest

from sorting.n_2824_count_pairs_whose_sum_is_less_than_target import (
    CountPairsWhoseSumIsLessThanTarget,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [-1, 1, 2, 3, 1]
        target = 2
        expected = 3
        self.assertEqual(
            expected, CountPairsWhoseSumIsLessThanTarget.solution(nums, target)
        )  # add assertion here

    def test_case_two(self):
        nums = [-6, 2, 5, -2, -7, -1, 3]
        target = -2
        expected = 10
        self.assertEqual(
            expected, CountPairsWhoseSumIsLessThanTarget.solution(nums, target)
        )


if __name__ == "__main__":
    unittest.main()
