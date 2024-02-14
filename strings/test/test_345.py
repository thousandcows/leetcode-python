import unittest

from strings.n_345_reverse_vowels_of_a_string import ReverseVowelsOfAString


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "hello"
        expected = "holle"
        self.assertEqual(
            expected, ReverseVowelsOfAString.solution(s)
        )  # add assertion here

    def test_case_two(self):
        s = "leetcode"
        expected = "leotcede"
        self.assertEqual(expected, ReverseVowelsOfAString.solution(s))

    def test_case_three(self):
        s = "aA"
        expected = "Aa"
        self.assertEqual(expected, ReverseVowelsOfAString.solution(s))

    def test_case_four(self):
        s = "a"
        expected = "a"
        self.assertEqual(expected, ReverseVowelsOfAString.solution(s))

    def test_case_five(self):
        s = "ccc"
        expected = "ccc"
        self.assertEqual(expected, ReverseVowelsOfAString.solution(s))


if __name__ == "__main__":
    unittest.main()
