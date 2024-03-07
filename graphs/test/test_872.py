import unittest

from graphs.n_872_leaf_similar_trees import LeafSimilarTrees
from graphs.treenode import TreeNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root1 = TreeNode(
            3,
            TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
            TreeNode(1, TreeNode(9), TreeNode(8)),
        )
        root2 = TreeNode(
            3,
            TreeNode(5, TreeNode(6), TreeNode(7)),
            TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8))),
        )
        expected = True
        self.assertEqual(
            True, LeafSimilarTrees.solution(root1, root2)
        )  # add assertion here

    def test_case_two(self):
        root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        root2 = TreeNode(1, TreeNode(3), TreeNode(2))
        expected = False
        self.assertEqual(expected, LeafSimilarTrees.solution(root1, root2))


if __name__ == "__main__":
    unittest.main()
