import unittest

from strings.n_1431_kids_with_the_greatest_number_of_candies import (
    KidsWithTheGreatestNumberOfCandies,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        candies = [2, 3, 5, 1, 3]
        extra_candies = 3
        expected = [True, True, True, False, True]
        self.assertEqual(
            expected,
            KidsWithTheGreatestNumberOfCandies.solution(candies, extra_candies),
        )  # add assertion here

    def test_case_two(self):
        candies = [4, 2, 1, 1, 2]
        extra_candies = 1
        expected = [True, False, False, False, False]
        self.assertEqual(
            expected,
            KidsWithTheGreatestNumberOfCandies.solution(candies, extra_candies),
        )

    def test_case_three(self):
        candies = [12, 1, 12]
        extra_candies = 10
        expected = [True, False, True]
        self.assertEqual(
            expected,
            KidsWithTheGreatestNumberOfCandies.solution(candies, extra_candies),
        )

    def test_case_four(self):
        candies = ([3, 3, 3, 3, 3],)
        extra_candies = 3
        expected = [True, True, True, True, True]
        self.assertEqual(
            expected,
            KidsWithTheGreatestNumberOfCandies.solution(candies, extra_candies),
        )


if __name__ == "__main__":
    unittest.main()
