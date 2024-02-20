import unittest

from arrays.n_1995_count_special_quadruplets import CountSpecialQuadruplets


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 2, 3, 4]
        expected = 1
        self.assertEqual(
            expected, CountSpecialQuadruplets.solution(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [3, 3, 6, 4, 5]
        expected = 0
        self.assertEqual(expected, CountSpecialQuadruplets.solution(nums))

    def test_case_three(self):
        nums = [1, 1, 1, 3, 5]
        expected = 4
        self.assertEqual(expected, CountSpecialQuadruplets.solution(nums))

    def test_case_four(self):
        nums = [2, 3]
        expected = 0
        self.assertEqual(expected, CountSpecialQuadruplets.solution(nums))


if __name__ == "__main__":
    unittest.main()
