import unittest

from backtracking.n_401_binary_watch import BinaryWatch


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        turn_on = 1
        expected = [
            "0:01",
            "0:02",
            "0:04",
            "0:08",
            "0:16",
            "0:32",
            "1:00",
            "2:00",
            "4:00",
            "8:00",
        ]
        self.assertEqual(
            expected, sorted(BinaryWatch.backtrack_solution(turn_on))
        )  # add assertion here

    def test_case_two(self):
        turn_on = 9
        expected = []
        self.assertEqual(expected, BinaryWatch.backtrack_solution(turn_on))


if __name__ == "__main__":
    unittest.main()
