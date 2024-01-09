import unittest

from array.n_561_array_partition import ArrayPartition


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 4, 3, 2]
        self.assertEqual(4, ArrayPartition.execute(nums))

    def test_caes_two(self):
        nums = [6, 2, 6, 5, 1, 2]
        self.assertEqual(9, ArrayPartition.execute(nums))

    def test_caes_three(self):
        nums = [i for i in range(1, 11)]
        self.assertEqual(25, ArrayPartition.execute(nums))


if __name__ == "__main__":
    unittest.main()
