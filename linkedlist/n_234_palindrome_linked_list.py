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
        reverse = None  # create a linklist to store the values in reverse order
        slow_runner = fast_runner = head  # initialize values

        # reverse the linklist using the runner concept
        while fast_runner and fast_runner.next:
            fast_runner = fast_runner.next.next
            reverse, reverse.next, slow_runner = slow_runner, reverse, slow_runner.next

        if fast_runner:
            slow_runner = slow_runner.next

        # check if the list is palindrome
        while reverse and reverse.val == slow_runner.val:
            slow_runner, reverse = slow_runner.next, reverse.next
        return not reverse
