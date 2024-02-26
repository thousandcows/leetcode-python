import unittest

from sliding_window.n_1493_longest_subarray_of_first_after_deleting_one_element import \
    LongestSubarrayOfFirstAfterDeletingOneElement


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 1, 0, 1]
        expected = 3
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))  # add assertion here

    def test_case_two(self):
        nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
        expected = 5
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))

    def test_case_three(self):
        nums = [1, 1, 1]
        expected = 2
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))

    def test_case_four(self):
        nums = [1,0,0,1,0]
        expected = 1
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))

    def test_case_five(self):
        nums = [1,0,0,0,0]
        expected = 1
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))

    def test_case_six(self):
        nums = [0,1,1,1,0,0,1,1,0]
        expected = 3
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))

    def test_case_seven(self):
        nums = [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1]
        expected = 18
        self.assertEqual(expected, LongestSubarrayOfFirstAfterDeletingOneElement.solution(nums))

if __name__ == '__main__':
    unittest.main()
