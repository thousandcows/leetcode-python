from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNodesInPair:
    @staticmethod
    @time_measurement
    def solution(head: ListNode | None) -> ListNode | None:
        # condition to end the recursion
        if head and head.next:
            p = head.next  # use p to store the second node
            head.next = SwapNodesInPair.solution(p.next)    # swap the rest of the list starting from head.next.next
            p.next = head   # set the head as the second node
            return p
        return head
