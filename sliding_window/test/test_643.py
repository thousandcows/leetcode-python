import unittest

from sliding_window.n_643_maximum_average_subarray_one import MaximumAverageSubarrayOne


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 4
        expected = 12.75000
        self.assertEqual(expected, MaximumAverageSubarrayOne.solution(nums, k))  # add assertion here

    def test_case_two(self):
        nums = [5]
        k = 1
        expected = 5.00000
        self.assertEqual(expected, MaximumAverageSubarrayOne.solution(nums, k))

    def test_case_three(self):
        nums = [0,1,1,3,3]
        k = 4
        expected = 2.00000
        self.assertEqual(expected, MaximumAverageSubarrayOne.solution(nums, k))

    def test_case_four(self):
        nums = [4,0,4,3,3]
        k = 5
        expected = 2.80000
        self.assertEqual(expected, MaximumAverageSubarrayOne.solution(nums, k))

if __name__ == '__main__':
    unittest.main()
