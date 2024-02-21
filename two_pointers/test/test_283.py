import unittest

from two_pointers.n_283_move_zeroes import MoveZeroes


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        self.assertEqual(expected, MoveZeroes.solution(nums))  # add assertion here

    def test_case_two(self):
        nums = [0]
        expected = [0]
        self.assertEqual(expected, MoveZeroes.solution(nums))

    def test_case_three(self):
        nums = [0, 0, 1]
        expected = [1, 0, 0]
        self.assertEqual(expected, MoveZeroes.solution(nums))

    def test_case_four(self):
        nums = [0] * 9999 + [1]
        expected = [1] + [0] * 9999
        self.assertEqual(expected, MoveZeroes.solution(nums))

if __name__ == '__main__':
    unittest.main()
