import unittest

from backtracking.n_1863_sum_of_all_subset_xor_totals import SumOfAllSubsetXORTotals


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 3]
        expected = 6
        self.assertEqual(
            expected, SumOfAllSubsetXORTotals.bitwise_solution(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [5, 1, 6]
        expected = 28
        self.assertEqual(expected, SumOfAllSubsetXORTotals.bitwise_solution(nums))

    def test_case_three(self):
        nums = [3, 4, 5, 6, 7, 8]
        expected = 480
        self.assertEqual(expected, SumOfAllSubsetXORTotals.bitwise_solution(nums))


if __name__ == "__main__":
    unittest.main()
