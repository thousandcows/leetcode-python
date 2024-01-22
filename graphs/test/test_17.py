import unittest

from graphs.n_17_letter_combination_of_a_phone_number import (
    LetterCombinationsOfAPhoneNumber,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        digits = "23"
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(
            expected, sorted(LetterCombinationsOfAPhoneNumber.solution(digits))
        )

    def test_case_two(self):
        digits = ""
        expected = []
        self.assertEqual(
            expected, sorted(LetterCombinationsOfAPhoneNumber.solution(digits))
        )

    def test_case_three(self):
        digits = "2"
        expected = ["a", "b", "c"]
        self.assertEqual(
            expected, sorted(LetterCombinationsOfAPhoneNumber.solution(digits))
        )

    def test_case_four(self):
        digits = "7"
        expected = ["p", "q", "r", "s"]
        self.assertEqual(
            expected, sorted(LetterCombinationsOfAPhoneNumber.solution(digits))
        )

    def test_case_five(self):
        digits = "2345"
        expected = [
            "adgj",
            "adgk",
            "adgl",
            "adhj",
            "adhk",
            "adhl",
            "adij",
            "adik",
            "adil",
            "aegj",
            "aegk",
            "aegl",
            "aehj",
            "aehk",
            "aehl",
            "aeij",
            "aeik",
            "aeil",
            "afgj",
            "afgk",
            "afgl",
            "afhj",
            "afhk",
            "afhl",
            "afij",
            "afik",
            "afil",
            "bdgj",
            "bdgk",
            "bdgl",
            "bdhj",
            "bdhk",
            "bdhl",
            "bdij",
            "bdik",
            "bdil",
            "begj",
            "begk",
            "begl",
            "behj",
            "behk",
            "behl",
            "beij",
            "beik",
            "beil",
            "bfgj",
            "bfgk",
            "bfgl",
            "bfhj",
            "bfhk",
            "bfhl",
            "bfij",
            "bfik",
            "bfil",
            "cdgj",
            "cdgk",
            "cdgl",
            "cdhj",
            "cdhk",
            "cdhl",
            "cdij",
            "cdik",
            "cdil",
            "cegj",
            "cegk",
            "cegl",
            "cehj",
            "cehk",
            "cehl",
            "ceij",
            "ceik",
            "ceil",
            "cfgj",
            "cfgk",
            "cfgl",
            "cfhj",
            "cfhk",
            "cfhl",
            "cfij",
            "cfik",
            "cfil",
        ]
        self.assertEqual(expected, LetterCombinationsOfAPhoneNumber.solution(digits))


if __name__ == "__main__":
    unittest.main()
