import unittest

from strings.n_937_reorder_log_files import ReorderLogs


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        input = [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
        output = [
            "let1 art can",
            "let3 art zero",
            "let2 own kit dig",
            "dig1 8 1 5 1",
            "dig2 3 6",
        ]

        self.assertEqual(output, ReorderLogs.execute(input))

    def test_case_two(self):
        input = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        output = [
            "g1 act car",
            "a8 act zoo",
            "ab1 off key dog",
            "a1 9 2 3 1",
            "zo4 4 7",
        ]

        self.assertEqual(output, ReorderLogs.execute(input))


if __name__ == "__main__":
    unittest.main()
