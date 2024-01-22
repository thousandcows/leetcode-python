import unittest

from hashtable.n_347_top_k_frequent_elements import TopKFrequentElements
from hashtable.n_347_top_k_frequent_elements_heapq import TopKFrequentElementsWithHeapq


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        output = (1, 2)
        self.assertEqual(
            output, TopKFrequentElements.solution(nums, k)
        )  # add assertion here

    def test_case_two(self):
        nums = [1]
        k = 1
        output = (1,)
        self.assertEqual(output, TopKFrequentElements.solution(nums, k))

    def test_case_three(self):
        nums = [1, 2]
        k = 2
        output = [1, 2]
        self.assertEqual(output, TopKFrequentElementsWithHeapq.solution(nums, k))

    def test_case_four(self):
        nums = [3, 0, 1, 0]
        k = 1
        output = [
            0,
        ]
        self.assertEqual(output, TopKFrequentElementsWithHeapq.solution(nums, k))


if __name__ == "__main__":
    unittest.main()
