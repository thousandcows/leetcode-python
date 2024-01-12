import unittest

from linkedlist.n_206_reverse_linked_list import ListNode
from linkedlist.n_2_add_two_numbers import AddTwoNumbers


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(2, ListNode(4)))
        answer: ListNode | None = AddTwoNumbers.solution(list1, list2)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = ["2", "4", "8"]
        self.assertEqual(output, expected)  # add assertion here

    def test_case_two(self):
        list1 = ListNode(9, ListNode(9, ListNode(9)))
        list2 = ListNode(1, ListNode(0, ListNode(1)))
        answer: ListNode | None = AddTwoNumbers.solution(list1, list2)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = ["0", "0", "1", "1"]
        self.assertEqual(output, expected)  # add assertion here

    def test_case_three(self):
        list1 = ListNode(0)
        list2 = ListNode(0)
        answer: ListNode | None = AddTwoNumbers.solution(list1, list2)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = ["0"]
        self.assertEqual(output, expected)  # add assertion here


if __name__ == "__main__":
    unittest.main()
