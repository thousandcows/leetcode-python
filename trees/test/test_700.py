import unittest

from graphs.treenode import TreeNode
from trees.n_700_search_binary_search_tree import SearchInABinarySearchTree


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        val = 2
        expected = 2
        output = SearchInABinarySearchTree.solution(root, val)
        self.assertEqual(expected, output.val)  # add assertion here

    def test_case_two(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        val = 5
        expected = None
        output = SearchInABinarySearchTree.solution(root, val)
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
