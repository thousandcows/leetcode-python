import unittest

from backtracking.test.n_257_binary_tree_path import BinaryTreePath
from graphs.treenode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
        expected = ["1->2->5", "1->3"]
        self.assertEqual(
            expected, sorted(BinaryTreePath.solution(root))
        )  # add assertion here

    def test_case_two(self):
        root = TreeNode(1)
        expected = ["1"]
        self.assertEqual(expected, sorted(BinaryTreePath.solution(root)))

    def test_case_three(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        expected = ["1->2", "1->3"]
        self.assertEqual(expected, sorted(BinaryTreePath.solution(root)))

    def test_case_four(self):
        root = TreeNode(1, TreeNode(2, None))
        expected = ["1->2"]
        self.assertEqual(expected, sorted(BinaryTreePath.solution(root)))


if __name__ == "__main__":
    unittest.main()
