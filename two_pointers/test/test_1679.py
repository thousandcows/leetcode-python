import unittest

from two_pointers.n_1679_max_number_of_k_sum_pairs import MaxNumberOfKSumPairs


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 2, 3, 4]
        k = 5
        expected = 2
        self.assertEqual(expected, MaxNumberOfKSumPairs.solution(nums, k))  # add assertion here

    def test_case_two(self):
        nums = [3, 1, 3, 4, 3]
        k = 6
        expected = 1
        self.assertEqual(expected, MaxNumberOfKSumPairs.solution(nums, k))


if __name__ == '__main__':
    unittest.main()
