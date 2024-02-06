import unittest

from strings.n_1071_greatest_common_divisor_of_strings import GCD


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        str1 = "ABCABC"
        str2 = "ABC"
        expected = "ABC"
        self.assertEqual(expected, GCD.solution(str1, str2))  # add assertion here

    def test_case_two(self):
        str1 = "ABABAB"
        str2 = "ABAB"
        expected = "AB"
        self.assertEqual(expected, GCD.solution(str1, str2))

    def test_case_three(self):
        str1 = "LEET"
        str2 = "CODE"
        expected = ""
        self.assertEqual(expected, GCD.solution(str1, str2))


if __name__ == "__main__":
    unittest.main()
