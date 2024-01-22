import unittest

from graphs.n_200_number_of_islands import NumberOfIslands


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        output = 1
        self.assertEqual(output, NumberOfIslands().solution(grid))  # add assertion here

    def test_case_two(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        output = 3
        self.assertEqual(output, NumberOfIslands().solution(grid))

    def test_case_three(self):
        grid = [["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]
        output = 4
        self.assertEqual(output, NumberOfIslands().solution(grid))

    def test_when_it_is_the_whole_island(self):
        grid = [["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]]
        output = 1
        self.assertEqual(output, NumberOfIslands().solution(grid))

    def test_when_there_is_no_island(self):
        grid = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        output = 0
        self.assertEqual(output, NumberOfIslands().solution(grid))


if __name__ == "__main__":
    unittest.main()
