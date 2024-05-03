import sys
import unittest

from programmers.sorting.가장큰수 import MaxNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        numbers = [6, 10, 2]
        expected = "6210"
        self.assertEqual(expected, MaxNumber.solution(numbers))  # add assertion here

    def test_case_two(self):
        numbers = [3, 30, 34, 5, 9]
        expected = "9534330"
        self.assertEqual(expected, MaxNumber.solution(numbers))

    def test_case_three(self):
        numbers = [0, 0, 0, 0]
        expected = "0"
        self.assertEqual(expected, MaxNumber.solution(numbers))

    def test_case_four(self):
        sys.set_int_max_str_digits(50000)
        numbers = [1, 9] * 20000
        expected = "9" * 20000 + "1" * 20000
        self.assertEqual(expected, MaxNumber.solution(numbers))


if __name__ == "__main__":
    unittest.main()
