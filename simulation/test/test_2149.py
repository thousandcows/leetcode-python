import unittest

from simulation.n_2149_rearrange_array_elements_by_sign import (
    RearrangeArrayElementsBySign,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [3, 1, -2, -5, 2, -4]
        expected = [3, -2, 1, -5, 2, -4]
        self.assertEqual(
            expected, RearrangeArrayElementsBySign.solution(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [-1, 1]
        expected = [1, -1]
        self.assertEqual(expected, RearrangeArrayElementsBySign.solution(nums))


if __name__ == "__main__":
    unittest.main()
