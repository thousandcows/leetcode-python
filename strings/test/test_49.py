import unittest

from strings.n_49_group_anagrams import GroupAnagrams


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertEqual(output, GroupAnagrams.execute(input))  # add assertion here

    def test_case_empty_list(self):
        input = [""]
        output = [[""]]
        self.assertEqual(output, GroupAnagrams.execute(input))  # add assertion here

    def test_case_min(self):
        input = ["e"]
        output = [["e"]]
        self.assertEqual(output, GroupAnagrams.execute(input))  # add assertion here


if __name__ == "__main__":
    unittest.main()
