import unittest

from simulation.n_67_add_binary import AddBinary


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        a = "111"
        b = "11"
        expected = "1010"
        self.assertEqual(expected, AddBinary.solution(a, b))  # add assertion here

    def test_case_two(self):
        a = "1010"
        b = "1011"
        expected = "10101"
        self.assertEqual(expected, AddBinary.solution(a, b))


if __name__ == "__main__":
    unittest.main()
