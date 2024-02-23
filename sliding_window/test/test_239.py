import unittest

from sliding_window.n_239_sliding_window_maximum import SlidingWindowMaximum


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [3, 3, 5, 5, 6, 7]
        self.assertEqual(expected, SlidingWindowMaximum.solution(nums, k))  # add assertion here

    def test_case_two(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(expected, SlidingWindowMaximum.solution(nums, k))




if __name__ == '__main__':
    unittest.main()
