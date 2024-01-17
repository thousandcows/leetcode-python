import unittest

from stack.stace_adt import Stack


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        for i in range(9, -1, -1):
            self.assertEqual(stack.pop(), i)  # add assertion here


if __name__ == "__main__":
    unittest.main()
