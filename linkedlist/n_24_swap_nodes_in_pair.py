from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNodesInPair:
    @staticmethod
    @time_measurement
    def solution(head: ListNode | None) -> ListNode | None:
        curr = head

        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next

        return head
