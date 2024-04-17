import unittest

from simulation.n_1389_create_target_array_in_the_given_order import (
    CreateTargetArrayInTheGivenOrder,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [0, 1, 2, 3, 4]
        index = [0, 1, 2, 2, 1]
        expected = [0, 4, 1, 3, 2]
        self.assertEqual(
            expected, CreateTargetArrayInTheGivenOrder.solution(nums, index)
        )  # add assertion here

    def test_case_two(self):
        nums = [1, 2, 3, 4, 0]
        index = [0, 1, 2, 3, 0]
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(
            expected, CreateTargetArrayInTheGivenOrder.solution(nums, index)
        )


if __name__ == "__main__":
    unittest.main()
