import unittest

from recursion.n_326_power_of_three import PowerOfThree


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 27
        expected = True
        self.assertEqual(expected, PowerOfThree.solution(n))  # add assertion here

    def test_case_two(self):
        n = 0
        expected = False
        self.assertEqual(expected, PowerOfThree.solution(n))

    def test_case_three(self):
        n = 9
        expected = True
        self.assertEqual(expected, PowerOfThree.solution(n))

    def test_case_four(self):
        n = 45
        expected = False
        self.assertEqual(expected, PowerOfThree.solution(n))


if __name__ == "__main__":
    unittest.main()
