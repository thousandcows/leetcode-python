import unittest

from simulation.n_1006_clumsy_factorial import ClumsyFactorial


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 4
        expected = 7
        self.assertEqual(expected, ClumsyFactorial.solution(n))  # add assertion here

    def test_case_two(self):
        n = 10
        expected = 12
        self.assertEqual(
            expected,
            ClumsyFactorial.solution(n),
        )


if __name__ == "__main__":
    unittest.main()
