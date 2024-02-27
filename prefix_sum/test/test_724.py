import unittest

from prefix_sum.n_724_find_pivot_index import FindPivotIndex


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 7, 3, 6, 5, 6]
        expected = 3
        self.assertEqual(expected, FindPivotIndex.solution(nums))  # add assertion here

    def test_case_two(self):
        nums = [1, 2, 3]
        expected = -1
        self.assertEqual(expected, FindPivotIndex.solution(nums))

    def test_case_three(self):
        nums = [2, 1, -1]
        expected = 0
        self.assertEqual(expected, FindPivotIndex.solution(nums))

    def test_case_four(self):
        nums = [0, 0, 0, 0]
        expected = 0
        self.assertEqual(expected, FindPivotIndex.solution(nums))

    def test_case_five(self):
        nums = [-1, -1, 1, 1, 0, 0]
        expected = 4
        self.assertEqual(expected, FindPivotIndex.solution(nums))


if __name__ == "__main__":
    unittest.main()
