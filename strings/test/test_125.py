import unittest

from strings.n_125_valid_palindrome import Solution


class MyTestCase(unittest.TestCase):
    def test_pure_palindrome(self):
        pure_palindrome = "ababa"
        self.assertEqual(True, Solution.is_palindrome(pure_palindrome))

    def test_non_palindrome(self):
        non_palindrome = "abaca"
        self.assertEqual(False, Solution.is_palindrome(non_palindrome))

    def test_palindrome_with_spaces(self):
        palindrome_with_spaces = "a    "
        self.assertEqual(True, Solution.is_palindrome(palindrome_with_spaces))

    def test_palindrome_with_non_alphanumerics(self):
        palindrome_with_non_alphanumerics = "a_ba ba!: = baba"
        self.assertEqual(
            True, Solution.is_palindrome(palindrome_with_non_alphanumerics)
        )


if __name__ == "__main__":
    unittest.main()
