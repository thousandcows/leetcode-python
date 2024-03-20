import unittest

from backtracking.n_797_all_paths_from_source_to_target import (
    AllPathsFromSourceToTarget,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        graph = [[1, 2], [3], [3], []]
        expected = [[0, 1, 3], [0, 2, 3]]
        self.assertEqual(
            expected, AllPathsFromSourceToTarget.solution(graph)
        )  # add assertion here

    def test_case_two(self):
        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        expected = [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
        self.assertEqual(expected, AllPathsFromSourceToTarget.solution(graph))


if __name__ == "__main__":
    unittest.main()
