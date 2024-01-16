import unittest

from linkedlist.n_24_swap_nodes_in_pair import SwapNodesInPair, ListNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        answer: ListNode | None = SwapNodesInPair.solution(head)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [2, 1, 4, 3]
        self.assertEqual(output, expected)  # add assertion here

    def test_case_two(self):
        head = ListNode(1)
        answer: ListNode | None = SwapNodesInPair.solution(head)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1]
        self.assertEqual(output, expected)

    def test_case_three(self):
        head = None
        answer: ListNode | None = SwapNodesInPair.solution(head)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = []
        self.assertEqual(output, expected)


if __name__ == "__main__":
    unittest.main()
