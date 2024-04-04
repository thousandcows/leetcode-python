from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeNodesInBetweenZeros:
    @staticmethod
    @time_measurement
    def solution(head: ListNode) -> ListNode:
        output, curr_node, before_node = None, head.next, None
        # 0 1 0 3 0 2 2 0
        while True:
            curr_sum = 0
            new_node = None
            while True:
                if curr_node.val == 0:
                    break
                curr_sum += curr_node.val
                curr_node = curr_node.next

            if curr_sum > 0:
                new_node = ListNode(curr_sum, None)

            if before_node is None:
                output, before_node = new_node, new_node
            elif new_node:
                before_node.next = new_node
                before_node = new_node

            if curr_node.next is None:
                break
            curr_node = curr_node.next

        return output
