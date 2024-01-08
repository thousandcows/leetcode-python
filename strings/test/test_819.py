import unittest

from strings.n_819_most_common_word import MostCommonWord


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        output = "ball"

        self.assertEqual(output, MostCommonWord.execute(paragraph, banned))

    def test_case_two(self):
        paragraph = "a."
        banned = []
        output = "a"

        self.assertEqual(output, MostCommonWord.execute(paragraph, banned))

    def test_case_the_longest(self):
        paragraph = "It hit a ball, the hit BALL flew far after it was hit." * 20
        banned = ["ball", "hit", "a"]
        output = "it"

        self.assertEqual(output, MostCommonWord.execute(paragraph, banned))

    def test_case_without_spaces(self):
        paragraph = "a, a, a, a, b,b,b,c, c"
        banned = ["a"]
        output = "b"

        self.assertEqual(output, MostCommonWord.execute(paragraph, banned))


if __name__ == "__main__":
    unittest.main()
