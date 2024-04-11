import unittest

from simulation.n_68_text_justification import TextJustification


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        max_width = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  ",
        ]
        self.assertEqual(
            expected, TextJustification.solution(words, max_width)
        )  # add assertion here

    def test_case_two(self):
        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        max_width = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        ",
        ]
        self.assertEqual(expected, TextJustification.solution(words, max_width))

    def test_case_three(self):
        words = [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ]
        max_width = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ]
        self.assertEqual(expected, TextJustification.solution(words, max_width))


if __name__ == "__main__":
    unittest.main()
