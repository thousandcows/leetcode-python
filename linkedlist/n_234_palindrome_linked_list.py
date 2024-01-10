from collections import deque
from typing import Optional

from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class PalindromeLinkedList:
    @staticmethod
    @time_measurement
    def solution(head: Optional[ListNode]) -> bool:
        if not head:
            return False

        q = deque()
        curr_head = head
        while curr_head:
            q.append(curr_head.val)
            curr_head = curr_head.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
