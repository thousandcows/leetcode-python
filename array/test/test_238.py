import unittest

from array.n_238_product_of_array_except_self import ProductOfArrayExceptSelf


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = [1, 2, 3, 4]
        output = [24, 12, 8, 6]
        self.assertEqual(
            output, ProductOfArrayExceptSelf.execute(nums)
        )  # add assertion here

    def test_case_two(self):
        nums = [-1, 1, 0, -3, 3]
        output = [0, 0, 9, 0, 0]
        self.assertEqual(output, ProductOfArrayExceptSelf.execute(nums))


if __name__ == "__main__":
    unittest.main()
