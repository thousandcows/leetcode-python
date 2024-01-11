import unittest

from linkedlist.n_21_merge_two_sorted_lists import MergeTwoSortedLists, ListNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        answer: ListNode | None = MergeTwoSortedLists.solution(list1, list2)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1, 1, 2, 3, 4, 4]
        self.assertEqual(output, expected)  # add assertion here

    def test_case_two(self):
        list1 = None
        list2 = ListNode(0)
        expected = list2

        self.assertEqual(
            MergeTwoSortedLists.solution(list1, list2), expected
        )  # add assertion here

    def test_case_three(self):
        list1 = None
        list2 = None
        expected = None
        self.assertEqual(
            MergeTwoSortedLists.solution(list1, list2), expected
        )  # add assertion here


if __name__ == "__main__":
    unittest.main()
