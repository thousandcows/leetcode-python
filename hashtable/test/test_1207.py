import unittest

from hashtable.n_1207_unique_number_of_occurrences import UniqueNumberOfOccurrences


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        arr = [1, 2, 2, 1, 1, 3]
        expected = True
        self.assertEqual(
            expected, UniqueNumberOfOccurrences.solution(arr)
        )  # add assertion here

    def test_case_two(self):
        arr = [1, 2]
        expected = False
        self.assertEqual(expected, UniqueNumberOfOccurrences.solution(arr))

    def test_case_three(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        expected = True
        self.assertEqual(expected, UniqueNumberOfOccurrences.solution(arr))


if __name__ == "__main__":
    unittest.main()
