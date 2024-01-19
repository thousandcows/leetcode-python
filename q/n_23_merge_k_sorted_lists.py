import heapq

from utils.time_measurement import time_measurement


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeKSortedLists:
    @staticmethod
    @time_measurement
    def solution(lists: list[ListNode] | None) -> ListNode | None:
        root = result = ListNode(None)

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
