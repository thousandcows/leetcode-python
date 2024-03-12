import unittest

from graphs.treenode import TreeNode
from trees.n_938_range_sum_of_bst import RangeSumOfBST


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(
            10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
        )
        low = 7
        high = 15
        expected = 32

        self.assertEqual(
            expected, RangeSumOfBST.solution(root, low, high)
        )  # add assertion here

    def test_case_two(self):
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
            TreeNode(15, TreeNode(13), TreeNode(18)),
        )
        low = 6
        high = 10
        expected = 23

        self.assertEqual(expected, RangeSumOfBST.solution(root, low, high))


if __name__ == "__main__":
    unittest.main()
