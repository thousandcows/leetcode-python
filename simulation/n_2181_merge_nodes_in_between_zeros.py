from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeNodesInBetweenZeros:
    @staticmethod
    @time_measurement
    def solution(head: ListNode) -> ListNode:
        output = head
        ptr = head.next
        curr_sum = 0

        while ptr.next:
            if ptr.val == 0:
                output.val = curr_sum
                output = output.next
                curr_sum = 0
            else:
                curr_sum += ptr.val
            ptr = ptr.next

        output.val = curr_sum
        output.next = None
        return head
