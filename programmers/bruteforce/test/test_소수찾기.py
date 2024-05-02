import unittest

from programmers.bruteforce.소수찻기 import FindPrimeNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        numbers = "17"
        expected = 3
        self.assertEqual(
            expected, FindPrimeNumber.solution(numbers)
        )  # add assertion here

    def test_case_two(self):
        numbers = "011"
        expected = 2
        self.assertEqual(expected, FindPrimeNumber.solution(numbers))

    def test_case_three(self):
        numbers = "123"
        expected = 5
        self.assertEqual(expected, FindPrimeNumber.solution(numbers))


if __name__ == "__main__":
    unittest.main()
