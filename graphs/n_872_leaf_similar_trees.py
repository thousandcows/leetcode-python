from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class LeafSimilarTrees:
    @staticmethod
    @time_measurement
    def solution(root1, root2) -> bool:
        def dfs(root: TreeNode, leafs: list) -> None:

            if not root:
                return

            if root.left is None and root.right is None:
                leafs.append(root.val)

            dfs(root.left, leafs)
            dfs(root.right, leafs)

        root1_list = []
        root2_list = []
        dfs(root1, root1_list)
        dfs(root2, root2_list)

        return root1_list == root2_list
