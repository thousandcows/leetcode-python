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

        word = [head.val]
        curr_head = head.next
        while curr_head:
            word.append(curr_head.val)
            curr_head = curr_head.next

        return word == word[::-1]
