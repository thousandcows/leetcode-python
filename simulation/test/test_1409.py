import unittest

from simulation.n_1409_queries_on_a_permutation_with_key import (
    QueriesOnAPermutationWithKey,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        queries = [3, 1, 2, 1]
        m = 5
        expected = [2, 1, 2, 1]
        self.assertEqual(
            expected, QueriesOnAPermutationWithKey.solution(queries, m)
        )  # add assertion here

    def test_case_two(self):
        queries = [4, 1, 2, 2]
        m = 4
        expected = [3, 1, 2, 0]
        self.assertEqual(expected, QueriesOnAPermutationWithKey.solution(queries, m))

    def test_case_three(self):
        queries = [7, 5, 5, 8, 3]
        m = 8
        expected = [6, 5, 0, 7, 5]
        self.assertEqual(expected, QueriesOnAPermutationWithKey.solution(queries, m))


if __name__ == "__main__":
    unittest.main()
