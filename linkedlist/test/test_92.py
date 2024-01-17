import unittest

from linkedlist.n_206_reverse_linked_list import ListNode
from linkedlist.n_92_reversed_linked_list import ReverseLinkedList


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        head = ListNode(2, None)
        answer: ListNode | None = ReverseLinkedList.solution(head, 1, 1)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [2]
        self.assertEqual(expected, output)  # add assertion here

    def test_case_two(self):
        head = ListNode(
            1,
            ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))),
        )
        answer: ListNode | None = ReverseLinkedList.solution(head, 2, 4)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1, 4, 3, 2, 5]
        self.assertEqual(expected, output)  # add assertion here


if __name__ == "__main__":
    unittest.main()
