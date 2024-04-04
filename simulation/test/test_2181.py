import unittest

from simulation.n_2181_merge_nodes_in_between_zeros import (
    ListNode,
    MergeNodesInBetweenZeros,
)


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        head = ListNode(
            0,
            ListNode(
                3,
                ListNode(
                    1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0)))))
                ),
            ),
        )
        expected = [4, 11]
        result = MergeNodesInBetweenZeros.solution(head)
        output = []
        while True:
            output.append(result.val)
            if result.next is None:
                break
            result = result.next

        self.assertEqual(expected, output)  # add assertion here

    def test_case_two(self):
        head = ListNode(
            0,
            ListNode(
                1,
                ListNode(
                    0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0)))))
                ),
            ),
        )
        expected = [1, 3, 4]
        result = MergeNodesInBetweenZeros.solution(head)
        output = []
        while True:
            output.append(result.val)
            if result.next is None:
                break
            result = result.next

        self.assertEqual(expected, output)  # add assertion here


if __name__ == "__main__":
    unittest.main()
