from typing import Optional

from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeTwoSortedLists:
    @staticmethod
    @time_measurement
    def solution(
        list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if (not list1) or (list2 and list2.val < list1.val):
            list1, list2 = list2, list1

        if list1:
            list1.next = MergeTwoSortedLists.solution(list1.next, list2)
        return list1
