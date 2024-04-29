import unittest

from programmers.bruteforce.모의고사 import TestExam


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        answers = [1, 2, 3, 4, 5]
        expected = [1]
        self.assertEqual(expected, TestExam.solution(answers))  # add assertion here

    def test_case_two(self):
        answers = [1, 3, 2, 4, 2]
        expected = [1, 2, 3]
        self.assertEqual(expected, TestExam.solution(answers))


if __name__ == "__main__":
    unittest.main()
