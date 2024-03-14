import unittest

from graphs.treenode import TreeNode
from trees.n_1161_maximum_level_sum_of_a_binary_tree import MaximumLevelSumOfABinaryTree


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
        expected = 2
        self.assertEqual(
            expected, MaximumLevelSumOfABinaryTree.solution(root)
        )  # add assertion here

    def test_case_two(self):
        root = TreeNode(
            989,
            TreeNode(10250, TreeNode(98693), TreeNode(-89388)),
            TreeNode(-87314, None, TreeNode(-95304)),
        )
        expected = 1
        self.assertEqual(expected, MaximumLevelSumOfABinaryTree.solution(root))


if __name__ == "__main__":
    unittest.main()
