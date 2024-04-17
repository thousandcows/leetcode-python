import unittest

from sorting.n_75_sort_colors import SortColors


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [2, 0, 2, 1, 1, 0]
        expected = [0, 0, 1, 1, 2, 2]
        self.assertEqual(expected, SortColors.solution(nums))  # add assertion here

    def test_case_two(self):
        nums = [2, 0, 1]
        expected = [0, 1, 2]
        self.assertEqual(expected, SortColors.solution(nums))

    def test_case_three(self):
        nums = [i for i in range(300, -1, -1)]
        expected = [i for i in range(301)]
        self.assertEqual(expected, SortColors.solution(nums))


if __name__ == "__main__":
    unittest.main()
