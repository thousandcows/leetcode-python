import unittest

from hashtable.n_347_top_k_frequent_elements import TopKFrequentElements


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


if __name__ == "__main__":
    unittest.main()
