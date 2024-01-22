import unittest

from hashtable.n_771_jewels_and_stones import JewelsAndStones


class MyTestCase(unittest.TestCase):
    def test_something(self):
        jewels, stones = "aA", "aAAbbbb"
        output = 3

        self.assertEqual(
            output, JewelsAndStones.solution(jewels, stones)
        )  # add assertion here

    def test_something2(self):
        jewels, stones = "z", "ZZ"
        output = 0

        self.assertEqual(output, JewelsAndStones.solution(jewels, stones))


if __name__ == "__main__":
    unittest.main()
