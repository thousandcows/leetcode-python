import unittest

from two_pointers.n_392_is_subsequence import IsSubsequence


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "abc"
        t = "ahbgdc"
        expected = True
        self.assertEqual(expected, IsSubsequence.solution(s, t))  # add assertion here

    def test_case_two(self):
        s = "axc"
        t = "ahbgdc"
        expected = False
        self.assertEqual(expected, IsSubsequence.solution(s, t))

if __name__ == '__main__':
    unittest.main()
