import unittest

from q.n_23_merge_k_sorted_lists import MergeKSortedLists, ListNode


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        lists = [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
        answer: ListNode | None = MergeKSortedLists.solution(lists)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(expected, output)  # add assertion here

    def test_case_two(self):
        lists = []
        answer: ListNode | None = MergeKSortedLists.solution(lists)
        output = []
        while answer:
            output.append(answer.val)
            answer = answer.next
        expected = []
        self.assertEqual(expected, output)


if __name__ == "__main__":
    unittest.main()
