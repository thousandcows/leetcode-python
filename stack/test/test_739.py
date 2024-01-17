import unittest

from stack.n_739_daily_temperatures import DailyTemperatures


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(
            [1, 1, 4, 2, 1, 1, 0, 0],
            DailyTemperatures.solution([73, 74, 75, 71, 69, 72, 76, 73]),
        )  # add assertion here

    def test_case_two(self):
        self.assertEqual(
            [1, 1, 1, 0],
            DailyTemperatures.solution([30, 40, 50, 60]),
        )

    def test_case_three(self):
        self.assertEqual(
            [1, 1, 0],
            DailyTemperatures.solution([30, 60, 90]),
        )

    def test_case_four(self):
        self.assertEqual(
            [0, 0, 0],
            DailyTemperatures.solution([30, 20, 10]),
        )


if __name__ == "__main__":
    unittest.main()
