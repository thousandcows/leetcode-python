import unittest

from simulation.n_2161_partition_array_according_to_given_pivot import (
    PartitionArrayAccordingToGivenPivot,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [9, 12, 5, 10, 14, 3, 10]
        pivot = 10
        expected = [9, 5, 3, 10, 10, 12, 14]
        self.assertEqual(
            expected, PartitionArrayAccordingToGivenPivot.solution(nums, pivot)
        )  # add assertion here

    def test_case_two(self):
        nums = [9, 12, 5, 10, 14, 3, 10]
        pivot = 9
        expected = [5, 3, 9, 12, 10, 14, 10]
        self.assertEqual(
            expected, PartitionArrayAccordingToGivenPivot.solution(nums, pivot)
        )


if __name__ == "__main__":
    unittest.main()
