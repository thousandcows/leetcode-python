import unittest

from backtracking.n_1079_letter_tile_possibilities import LetterTilePossibilities


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        tiles = "AAB"
        expected = 8
        self.assertEqual(
            expected, LetterTilePossibilities.solution(tiles)
        )  # add assertion here

    def test_case_two(self):
        tiles = "AAABBC"
        expected = 188
        self.assertEqual(expected, LetterTilePossibilities.solution(tiles))

    def test_case_three(self):
        tiles = "V"
        expected = 1
        self.assertEqual(expected, LetterTilePossibilities.solution(tiles))

    def test_case_four(self):
        tiles = "AZ"
        expected = 4
        self.assertEqual(expected, LetterTilePossibilities.solution(tiles))


if __name__ == "__main__":
    unittest.main()
