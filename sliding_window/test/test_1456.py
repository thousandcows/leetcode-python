import unittest

from sliding_window.n_1456_maximum_number_of_vowels_in_a_given_length import MaximumNumberOfVowelsInAGivenLength


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "abciiidef"
        k = 3
        expected = 3
        self.assertEqual(expected, MaximumNumberOfVowelsInAGivenLength.solution(s, k))  # add assertion here

    def test_case_two(self):
        s = "aeiou"
        k = 2
        expected = 2
        self.assertEqual(expected, MaximumNumberOfVowelsInAGivenLength.solution(s, k))

    def test_case_three(self):
        s = "leetcode"
        k = 3
        expected = 2
        self.assertEqual(expected, MaximumNumberOfVowelsInAGivenLength.solution(s, k))


if __name__ == '__main__':
    unittest.main()
