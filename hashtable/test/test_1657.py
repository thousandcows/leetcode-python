import unittest

from hashtable.n_1657_determine_if_two_strings_are_close import (
    DetermineIfTwoStringsAreClose,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        word1 = "abc"
        word2 = "bca"
        expected = True
        self.assertEqual(
            expected, DetermineIfTwoStringsAreClose.solution(word1, word2)
        )  # add assertion here

    def test_case_two(self):
        word1 = "a"
        word2 = "aa"
        expected = False
        self.assertEqual(expected, DetermineIfTwoStringsAreClose.solution(word1, word2))

    def test_case_three(self):
        word1 = "cabbba"
        word2 = "abbccc"
        expected = True
        self.assertEqual(expected, DetermineIfTwoStringsAreClose.solution(word1, word2))

    def test_case_four(self):
        word1 = "cabbb"
        word2 = "aabbc"
        expected = False
        self.assertEqual(expected, DetermineIfTwoStringsAreClose.solution(word1, word2))


if __name__ == "__main__":
    unittest.main()
