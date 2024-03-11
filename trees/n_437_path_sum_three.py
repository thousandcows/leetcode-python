from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class PathSumThree:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode, target_sum: int) -> int:
        def dfs(node, current_sum):
            nonlocal count
            if node is None:
                return

            current_sum += node.val
            count += prefix_sum.get(current_sum - target_sum, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            prefix_sum[current_sum] -= 1

        count = 0
        prefix_sum = {0: 1}
        dfs(root, 0)
        return count
