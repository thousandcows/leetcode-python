import unittest

from simulation.n_1688_count_of_matches_in_tournament import CountOfMatchesInTournament


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 7
        expected = 6
        self.assertEqual(
            expected, CountOfMatchesInTournament.solution(n)
        )  # add assertion here

    def test_case_two(self):
        n = 14
        expected = 13
        self.assertEqual(expected, CountOfMatchesInTournament.solution(n))


if __name__ == "__main__":
    unittest.main()
