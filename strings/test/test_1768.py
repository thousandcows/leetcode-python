import unittest

from strings.n_1768_merge_strings_alternately import MergeStringsAlternately


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        input_one = "abc"
        input_two = "pqr"
        expected = "apbqcr"
        self.assertEqual(
            expected, MergeStringsAlternately.solution(input_one, input_two)
        )  # add assertion here

    def test_case_two(self):
        input_one = "ab"
        input_two = "pqrs"
        expected = "apbqrs"
        self.assertEqual(
            expected, MergeStringsAlternately.solution(input_one, input_two)
        )

    def test_case_three(self):
        input_one = "abcd"
        input_two = "pq"
        expected = "apbqcd"
        self.assertEqual(
            expected, MergeStringsAlternately.solution(input_one, input_two)
        )


if __name__ == "__main__":
    unittest.main()
