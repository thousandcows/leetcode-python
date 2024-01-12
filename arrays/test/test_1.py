import unittest

from arrays.n_1_two_sum import TwoSome


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [[0, 1], [1, 0]]
        self.assertIn(TwoSome.execute(nums, target), expected)

    def test_case_two(self):
        nums = [3, 2, 4]
        target = 6
        expected = [[1, 2], [2, 1]]
        self.assertIn(TwoSome.execute(nums, target), expected)

    def test_case_three(self):
        nums = [3, 3]
        target = 6
        expected = [[0, 1], [1, 0]]
        self.assertIn(TwoSome.execute(nums, target), expected)


if __name__ == "__main__":
    unittest.main()
