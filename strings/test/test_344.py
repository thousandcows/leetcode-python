import unittest

from strings.n_344_reverse_string import ReverseString


class MyTestCase(unittest.TestCase):
    def test_hello(self):
        target = ["h", "e", "l", "l", "o"]
        answer = ["o", "l", "l", "e", "h"]
        ReverseString.execute(target)
        self.assertEqual(answer, target)

    def test_hannah(self):
        target = ["H", "a", "n", "n", "a", "h"]
        answer = ["h", "a", "n", "n", "a", "H"]
        ReverseString.execute(target)
        self.assertEqual(answer, target)

    def test_min(self):
        target = ["H"]
        answer = ["H"]
        ReverseString.execute(target)
        self.assertEqual(answer, target)

    def test_longest(self):
        target = ["H", "a", "n", "n", "a", "h"] * 2000
        answer = ["h", "a", "n", "n", "a", "H"] * 2000
        ReverseString.execute(target)
        self.assertEqual(answer, target)


if __name__ == "__main__":
    unittest.main()
