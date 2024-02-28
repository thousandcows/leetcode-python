import unittest

from hashtable.n_2215_find_the_difference_of_two_arrays import (
    FindTheDifferenceOfTwoArrays,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        expected = [[1, 3], [4, 6]]
        self.assertEqual(expected, FindTheDifferenceOfTwoArrays.solution(nums1, nums2))

    def test_case_two(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        expected = [[3], []]
        self.assertEqual(expected, FindTheDifferenceOfTwoArrays.solution(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
