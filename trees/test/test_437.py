import unittest

from graphs.treenode import TreeNode
from trees.n_437_path_sum_three import PathSumThree


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        root = TreeNode(
            10,
            TreeNode(
                5,
                TreeNode(3, TreeNode(3), TreeNode(-2)),
                TreeNode(2, None, TreeNode(1)),
            ),
            TreeNode(-3, None, TreeNode(11)),
        )
        target_sum = 8
        expected = 3
        self.assertEqual(
            expected, PathSumThree.solution(root, target_sum)
        )  # add assertion here

    def test_case_two(self):
        root = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
        target_sum = 3
        expected = 2
        self.assertEqual(expected, PathSumThree.solution(root, target_sum))

    def test_case_three(self):
        root = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None),
            TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
        )
        target_sum = 22
        expected = 3
        self.assertEqual(expected, PathSumThree.solution(root, target_sum))

    def test_case_four(self):
        root = TreeNode(
            1,
            None,
            TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))),
        )
        target_sum = 3
        expected = 2
        self.assertEqual(expected, PathSumThree.solution(root, target_sum))


if __name__ == "__main__":
    unittest.main()
