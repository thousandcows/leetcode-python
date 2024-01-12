import unittest

from linkedlist.n_206_reverse_linked_list import ReverseLinkedList, ListNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        answer: ListNode | None = ReverseLinkedList.solution(list1)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [4, 2, 1]
        self.assertEqual(output, expected)  # add assertion here

    def test_case_two(self):
        list1 = ListNode(1, None)
        answer: ListNode | None = ReverseLinkedList.solution(list1)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1]
        self.assertEqual(output, expected)  # add assertion here

    def test_case_three(self):
        list1 = None
        answer: ListNode | None = ReverseLinkedList.solution(list1)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = []
        self.assertEqual(output, expected)  # add assertion here


if __name__ == "__main__":
    unittest.main()
