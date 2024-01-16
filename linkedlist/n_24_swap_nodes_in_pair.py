from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNodesInPair:
    @staticmethod
    @time_measurement
    def solution(head: ListNode | None) -> ListNode | None:
        if head and head.next:
            p = head.next
            head.next = SwapNodesInPair.solution(p.next)
            p.next = head
            return p
        return head
