import unittest

from backtracking.n_1980_find_unique_binary_string import FindUniqueBinaryString


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        nums = ["01", "10"]
        assert FindUniqueBinaryString.solution(nums) not in nums

    def test_case_two(self):
        nums = ["00", "01"]
        assert FindUniqueBinaryString.solution(nums) not in nums

    def test_case_three(self):
        nums = ["111", "011", "001"]
        assert FindUniqueBinaryString.solution(nums) not in nums


if __name__ == "__main__":
    unittest.main()
