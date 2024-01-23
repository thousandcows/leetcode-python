import unittest

from graphs.n_39_combination_sum import CombinationSum


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        self.assertEqual(
            expected, CombinationSum.solution(candidates, target)
        )  # add assertion here

    def test_case_two(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(expected, CombinationSum.solution(candidates, target))

    def test_case_three(self):
        candidates = [2]
        target = 1
        expected = []
        self.assertEqual(expected, CombinationSum.solution(candidates, target))


if __name__ == "__main__":
    unittest.main()
