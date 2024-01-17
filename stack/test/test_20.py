import unittest

from stack.n_20_valid_parentheses import ValidParentheses


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(ValidParentheses.solution("()"), True)  # add assertion here

    def test_case_two(self):
        self.assertEqual(
            ValidParentheses.solution("()[]{}"), True
        )  # add assertion here

    def test_case_three(self):
        self.assertEqual(ValidParentheses.solution("(]"), False)  # add assertion here

    def test_case_four(self):
        self.assertEqual(ValidParentheses.solution("(][)"), False)  # add assertion here

    def test_case_five(self):
        self.assertEqual(
            ValidParentheses.solution("((([{}])))"), True
        )  # add assertion here


if __name__ == "__main__":
    unittest.main()
