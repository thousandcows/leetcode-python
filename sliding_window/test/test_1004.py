import unittest

from sliding_window.n_1004_max_consecutive_ones import MaxConsecutiveOnes


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums =[1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        expected = 6
        self.assertEqual(expected, MaxConsecutiveOnes.solution(nums, k))  # add assertion here

    def test_case_two(self):
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        expected = 10
        self.assertEqual(expected, MaxConsecutiveOnes.solution(nums, k))

if __name__ == '__main__':
    unittest.main()
