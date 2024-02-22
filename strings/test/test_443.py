import unittest

from strings.n_443_string_compression import StringCompression


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        expected = 6
        self.assertEqual(expected, StringCompression.solution(chars))  # add assertion here

    def test_case_two(self):
        chars = ["a"]
        expected = 1
        self.assertEqual(expected, StringCompression.solution(chars))

    def test_case_three(self):
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        expected = 4
        self.assertEqual(expected, StringCompression.solution(chars))

    def test_case_four(self):
        chars = ["a","a","a","b","b","a","a"]
        expected = 6
        self.assertEqual(expected, StringCompression.solution(chars))

    def test_case_five(self):
        chars = ["p","p","p","p","m","m","b","b","b","b","b","u","u","r","r","u","n","n","n","n","n","n","n","n","n","n","n","u","u","u","u","a","a","u","u","r","r","r","s","s","a","a","y","y","y","g","g","g","g","g"]
        expected = 30
        self.assertEqual(expected, StringCompression.solution(chars))

if __name__ == '__main__':
    unittest.main()
