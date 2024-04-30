import unittest

from programmers.hashtable.포켓몬 import Pokemon


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [3, 1, 2, 3]
        expected = 2
        self.assertEqual(expected, Pokemon.solution(nums))  # add assertion here

    def test_case_two(self):
        nums = [3, 3, 3, 2, 2, 4]
        expected = 3
        self.assertEqual(expected, Pokemon.solution(nums))

    def test_case_three(self):
        nums = [3, 3, 3, 2, 2, 2]
        expected = 2
        self.assertEqual(expected, Pokemon.solution(nums))


if __name__ == "__main__":
    unittest.main()
