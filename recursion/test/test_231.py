import unittest

from recursion.n_231_power_of_two import PowerOfTwo


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        input = 1
        expected = True
        self.assertEqual(expected, PowerOfTwo.solution(input))  # add assertion here

    def test_case_two(self):
        input = 16
        expected = True
        self.assertEqual(expected, PowerOfTwo.solution(input))

    def test_case_three(self):
        input = 3
        expected = False
        self.assertEqual(expected, PowerOfTwo.solution(input))

    def test_case_four(self):
        input = -4
        expected = False
        self.assertEqual(expected, PowerOfTwo.solution(input))

    def test_case_five(self):
        input = pow(2, 31) - 1
        expected = False
        self.assertEqual(expected, PowerOfTwo.solution(input))


if __name__ == "__main__":
    unittest.main()
