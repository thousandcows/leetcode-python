import unittest

from strings.n_3_longest_substring_witihout_reapeating_characters import (
    LongestSubstringWithoutRepeatingCharacters,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "abcababaaa"
        expected = 3
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )  # add assertion here

    def test_case_two(self):
        s = "bbbbbbb"
        expected = 1
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )

    def test_case_three(self):
        s = "pwwkew"
        expected = 3
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )

    def test_case_four(self):
        s = "abba"
        expected = 2
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )

    def test_case_five(self):
        s = " "
        expected = 1
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )

    def test_case_six(self):
        s = "abcdefghijklmnopqrstuvwxyz" * 10000
        expected = 26
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )

    def test_case_seven(self):
        s = "dvdf"
        expected = 3
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )

    def test_case_eight(self):
        s = "anviaj"
        expected = 5
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(s)
        )


if __name__ == "__main__":
    unittest.main()
