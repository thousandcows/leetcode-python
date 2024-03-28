import unittest

from dynamic_programming.n_70_climbing_stairs import ClimbingStairs


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 2
        expected = 2
        self.assertEqual(expected, ClimbingStairs.solution(n))  # add assertion here

    def test_case_two(self):
        n = 3
        expected = 3
        self.assertEqual(expected, ClimbingStairs.solution(n))

    def test_case_three(self):
        n = 4
        expected = 5
        self.assertEqual(expected, ClimbingStairs.solution(n))


if __name__ == "__main__":
    unittest.main()
