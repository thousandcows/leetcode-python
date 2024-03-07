import unittest

from graphs.n_104_maximum_depth_of_binary_tree import MaximumDepthOfBinaryTree
from graphs.treenode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected = 3
        self.assertEqual(
            expected, MaximumDepthOfBinaryTree.solution(root)
        )  # add assertion here

    def test_case_two(self):
        root = TreeNode(1, TreeNode(2), None)
        expected = 2
        self.assertEqual(expected, MaximumDepthOfBinaryTree.solution(root))


if __name__ == "__main__":
    unittest.main()
