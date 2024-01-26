import unittest

from recursion.n_509_fibonacci_number import FibonacciNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 2
        expected = 1
        self.assertEqual(expected, FibonacciNumber.solution(n))  # add assertion here

    def test_case_two(self):
        n = 3
        expected = 2
        self.assertEqual(expected, FibonacciNumber.solution(n))

    def test_case_three(self):
        n = 4
        expected = 3
        self.assertEqual(expected, FibonacciNumber.solution(n))

    def test_case_four(self):
        n = 0
        expected = 0
        self.assertEqual(expected, FibonacciNumber.solution(n))

    def test_case_five(self):
        n = 1
        expected = 1
        self.assertEqual(expected, FibonacciNumber.solution(n))


if __name__ == "__main__":
    unittest.main()
