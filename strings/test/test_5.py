import unittest

from strings.n_5_logest_palindromic_substring import LongestPalindromicSubstring


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "babad"
        answer = "bab"
        self.assertEqual(answer, LongestPalindromicSubstring.execute(s))

    def test_case_two(self):
        s = "cbbd"
        answer = "bb"
        self.assertEqual(answer, LongestPalindromicSubstring.execute(s))

    def test_case_min(self):
        s = "a"
        answer = "a"
        self.assertEqual(answer, LongestPalindromicSubstring.execute(s))

    def test_case_max(self):
        s = "a" * 990 + "b" * 10
        answer = "a" * 990
        self.assertEqual(answer, LongestPalindromicSubstring.execute(s))


if __name__ == "__main__":
    unittest.main()
