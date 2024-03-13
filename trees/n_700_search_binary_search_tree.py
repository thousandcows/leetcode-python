from graphs.treenode import TreeNode
from utils.time_measurement import time_measurement


class SearchInABinarySearchTree:
    @staticmethod
    @time_measurement
    def solution(root: TreeNode, val: int) -> TreeNode | None:
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            return SearchInABinarySearchTree.solution(root.left, val)
        else:
            return SearchInABinarySearchTree.solution(root.right, val)
