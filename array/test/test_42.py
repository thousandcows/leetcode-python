import unittest

from array.n_42_trapping_rain_water import TrappingRainWater


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        self.assertEqual(
            expected, TrappingRainWater.execute(height)
        )  # add assertion here

    def test_case_two(self):
        height = [4, 2, 0, 3, 2, 5]
        expected = 9
        self.assertEqual(
            expected, TrappingRainWater.execute(height)
        )  # add assertion here

    def test_case_three(self):
        height = [1, 1, 1]
        expected = 0
        self.assertEqual(
            expected, TrappingRainWater.execute(height)
        )  # add assertion here

    def test_case_four(self):
        height = [1, 2, 3, 4, 5]
        expected = 0
        self.assertEqual(expected, TrappingRainWater.execute(height))


if __name__ == "__main__":
    unittest.main()
