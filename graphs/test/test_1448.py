import unittest

from graphs.n_1448_count_good_nodes_in_binary_tree import CountGoodNodesInBinaryTree
from graphs.treenode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(
            3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5))
        )
        expected = 4
        self.assertEqual(
            expected, CountGoodNodesInBinaryTree.solution(root)
        )  # add assertion here

    def test_case_two(self):
        root = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
        expected = 3
        self.assertEqual(expected, CountGoodNodesInBinaryTree.solution(root))


if __name__ == "__main__":
    unittest.main()
