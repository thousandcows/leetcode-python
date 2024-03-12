from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class RangeSumOfBST:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode):
            nonlocal total, low, high
            if node is None:
                return

            if low <= node.val <= high:
                total += node.val
            dfs(node.left)
            dfs(node.right)

        total = 0
        dfs(root)
        return total
