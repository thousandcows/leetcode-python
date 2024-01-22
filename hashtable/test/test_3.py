import unittest

from hashtable.n_3_longest_substring_without_repeating_characters import (
    LongestSubstringWithoutRepeatingCharacters,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        input = "abcabcbb"
        expected = 3
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(input)
        )  # add assertion here

    def test_case_two(self):
        input = "bbbbb"
        expected = 1
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(input)
        )

    def test_case_three(self):
        input = "pwwkew"
        expected = 3
        self.assertEqual(
            expected, LongestSubstringWithoutRepeatingCharacters.solution(input)
        )


if __name__ == "__main__":
    unittest.main()
