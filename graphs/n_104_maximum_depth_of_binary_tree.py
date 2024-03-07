from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class MaximumDepthOfBinaryTree:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None) -> int:
            if node is None:
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)
