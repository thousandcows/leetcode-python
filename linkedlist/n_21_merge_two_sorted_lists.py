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
        # exception handling 1 - both list is None
        if not list1 and not list2:
            return None

        # exception handling 2 - only one list is None
        if not all((list1, list2)):
            return list1 or list2

        # append the values of each node one array for sorting
        li = []
        while list1:
            li.append(list1.val)
            list1 = list1.next

        while list2:
            li.append(list2.val)
            list2 = list2.next

        # Make the list to the linked list
        li.sort(reverse=True)

        answer = ListNode(li[0], None)
        for i, v in enumerate(li[1:]):
            node = ListNode(v, answer)
            answer = node

        return answer
