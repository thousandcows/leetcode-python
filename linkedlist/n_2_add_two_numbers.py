from typing import Optional

from utils.time_measurement import time_measurement


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    @staticmethod
    @time_measurement
    def solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # method that reverses the nodes
        def convert_linked_list_to_string(curr: ListNode, prev=None) -> str:
            str_value = ""
            while curr:
                str_value += str(curr.val)
                curr = curr.next

            return str_value[::-1]

        # method that creates the list to the list node
        def create(output_list: list) -> ListNode:
            head = prev = ListNode(output_list[0])

            for i, n in enumerate(output_list[1:]):
                curr = ListNode(n)
                prev.next = curr
                prev = curr

            return head

        num_one = convert_linked_list_to_string(l1)  # 342
        num_two = convert_linked_list_to_string(l2)  # 465

        total = str(int(num_one) + int(num_two))[::-1]  # 708

        node = create([w for w in total])
        return node
