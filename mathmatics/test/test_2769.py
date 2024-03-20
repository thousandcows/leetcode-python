import unittest

from mathmatics.n_find_the_maximum_achievable_number import (
    FindTheMaximumAchievableNumber,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        num = 4
        t = 1
        expected = 6
        self.assertEqual(
            expected, FindTheMaximumAchievableNumber.solution(num, t)
        )  # add assertion here

    def test_case_two(self):
        num = 3
        t = 2
        expected = 7
        self.assertEqual(expected, FindTheMaximumAchievableNumber.solution(num, t))

    def test_case_three(self):
        num = 2
        t = 4
        expected = 10
        self.assertEqual(expected, FindTheMaximumAchievableNumber.solution(num, t))


if __name__ == "__main__":
    unittest.main()
