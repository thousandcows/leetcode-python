from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class CountGoodNodesInBinaryTree:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode) -> int:

        def dfs(node: TreeNode | None, max_val: int):
            nonlocal output
            if not node:
                return

            if node.val >= max_val:
                output += 1
            max_val = max(node.val, max_val)

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        output = 0
        dfs(root, root.val)
        return output
