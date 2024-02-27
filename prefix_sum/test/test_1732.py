import unittest

from prefix_sum.n_1732_find_the_highest_altitude import FindTheHighestAltitude


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        gain = [-5, 1, 5, 0, -7]
        expected = 1
        self.assertEqual(
            expected, FindTheHighestAltitude.solution(gain)
        )  # add assertion here

    def test_case_two(self):
        gain = [-4, -3, -2, -1, 4, 3, 2]
        expected = 0
        self.assertEqual(expected, FindTheHighestAltitude.solution(gain))


if __name__ == "__main__":
    unittest.main()
