import unittest

from hashtable.n_1365_how_many_numbers_are_smaller_than_the_current_number import (
    HowManyNumbersAreSmallerThanTheCurrentNumber,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [8, 1, 2, 2, 3]
        expected = [4, 0, 1, 1, 3]
        self.assertEqual(
            expected,
            HowManyNumbersAreSmallerThanTheCurrentNumber.pythonic_solution(nums),
        )  # add assertion here

    def test_case_two(self):
        nums = [6, 5, 4, 8]
        expected = [2, 1, 0, 3]
        self.assertEqual(
            expected,
            HowManyNumbersAreSmallerThanTheCurrentNumber.pythonic_solution(nums),
        )

    def test_case_three(self):
        nums = [7, 7, 7, 7]
        expected = [0, 0, 0, 0]
        self.assertEqual(
            expected,
            HowManyNumbersAreSmallerThanTheCurrentNumber.pythonic_solution(nums),
        )


if __name__ == "__main__":
    unittest.main()
