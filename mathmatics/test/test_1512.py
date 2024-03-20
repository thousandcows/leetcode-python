import unittest

from mathmatics.n_1512_number_of_good_pairs import NumberOfGoodPairs


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 2, 3, 1, 1, 3]
        expected = 4
        self.assertEqual(
            expected, NumberOfGoodPairs.solution(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [1, 1, 1, 1]
        expected = 6
        self.assertEqual(expected, NumberOfGoodPairs.solution(nums))

    def test_case_three(self):
        nums = [1, 2, 3]
        expected = 0
        self.assertEqual(expected, NumberOfGoodPairs.solution(nums))

    def test_case_four(self):
        nums = [1]
        expected = 0
        self.assertEqual(expected, NumberOfGoodPairs.solution(nums))


if __name__ == "__main__":
    unittest.main()
