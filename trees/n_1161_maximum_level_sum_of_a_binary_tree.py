from collections import defaultdict

from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class MaximumLevelSumOfABinaryTree:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode) -> int:
        def dfs(node, level):
            if node is None:
                return
            sum_dict[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        sum_dict = defaultdict(int)
        dfs(root, 1)
        return sorted(sum_dict.items(), key=lambda kv: -kv[1])[0][0]
