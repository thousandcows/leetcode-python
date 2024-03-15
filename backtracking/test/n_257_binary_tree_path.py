from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class BinaryTreePath:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode) -> list[str]:
        def backtrack(node, path):
            # Dead end
            if node is None:
                return

            # Partial solution
            path += str(node.val) if path == "" else "->" + str(node.val)

            # Decision point
            if node.left is None and node.right is None:
                # Solution
                output.append(path)
                return

            # Backtrack
            backtrack(node.left, path)
            backtrack(node.right, path)

        output = []
        backtrack(root, "")
        return output
