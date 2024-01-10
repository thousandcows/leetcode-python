import unittest

from linkedlist.n_234_palindrome_linked_list import PalindromeLinkedList, ListNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        head = ListNode(
            val=1, next=ListNode(val=2, next=ListNode(val=2, next=ListNode(val=1)))
        )
        self.assertEqual(
            True, PalindromeLinkedList.solution(head)
        )  # add assertion here

    def test_case_two(self):
        head = ListNode(val=1, next=ListNode(val=2, next=None))
        self.assertEqual(False, PalindromeLinkedList.solution(head))

    def test_case_three(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2, next=ListNode(val=3, next=ListNode(val=2, next=ListNode(val=1)))
            ),
        )
        self.assertEqual(True, PalindromeLinkedList.solution(head))


if __name__ == "__main__":
    unittest.main()
