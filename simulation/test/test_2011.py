import unittest

from simulation.n_2011_final_value_of_variable_after_performing_operations import (
    FinalValueOfVariableAfterPerformingOperations,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        operations = ["X--", "X++", "--X"]
        expected = -1
        self.assertEqual(
            expected, FinalValueOfVariableAfterPerformingOperations.solution(operations)
        )  # add assertion here

    def test_case_two(self):
        operations = ["++X", "++X", "X++"]
        expected = 3
        self.assertEqual(
            expected, FinalValueOfVariableAfterPerformingOperations.solution(operations)
        )

    def test_case_three(self):
        operations = ["X++", "++X", "--X", "X--"]
        expected = 0
        self.assertEqual(
            expected, FinalValueOfVariableAfterPerformingOperations.solution(operations)
        )

    def test_case_four(self):
        operations = ["X++"] * 100
        expected = 100
        self.assertEqual(
            expected, FinalValueOfVariableAfterPerformingOperations.solution(operations)
        )


if __name__ == "__main__":
    unittest.main()
