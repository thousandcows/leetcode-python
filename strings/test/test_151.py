import unittest

from strings.n_151_reverse_words_in_a_string import ReverseWordsInAString


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "the sky is blue"
        expected = "blue is sky the"
        self.assertEqual(
            expected, ReverseWordsInAString.solution(s)
        )  # add assertion here

    def test_case_two(self):
        s = "  hello world  "
        expected = "world hello"
        self.assertEqual(expected, ReverseWordsInAString.solution(s))

    def test_case_three(self):
        s = "a good   example"
        expected = "example good a"
        self.assertEqual(expected, ReverseWordsInAString.solution(s))

    def test_case_four(self):
        s = "  Bob    Loves  Alice   12341234123412341234"
        expected = "12341234123412341234 Alice Loves Bob"
        self.assertEqual(expected, ReverseWordsInAString.solution(s))


if __name__ == "__main__":
    unittest.main()
