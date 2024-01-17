import unittest

from linkedlist.n_328_odd_even_linked_list import OddEvenLinkedList, ListNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        head = ListNode(
            2,
            ListNode(
                1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))
            ),
        )
        answer: ListNode | None = OddEvenLinkedList.solution(head)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [2, 3, 6, 7, 1, 5, 4]
        self.assertEqual(expected, output)  # add assertion here

    def test_case_two(self):
        head = ListNode(
            1,
            ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))),
        )
        answer: ListNode | None = OddEvenLinkedList.solution(head)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1, 3, 5, 2, 4]
        self.assertEqual(expected, output)  # add assertion here

    def test_case_three(self):
        head = ListNode(
            1,
            ListNode(3, ListNode(5, ListNode(7, None))),
        )
        answer: ListNode | None = OddEvenLinkedList.solution(head)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1, 5, 3, 7]
        self.assertEqual(expected, output)  # add assertion here


if __name__ == "__main__":
    unittest.main()
