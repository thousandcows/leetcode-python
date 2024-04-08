import unittest

from simulation.n_289_game_of_life import GameOfLife


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        GameOfLife.solution(board)
        self.assertEqual(expected, board)  # add assertion here

    def test_case_two(self):
        board = [[1, 1], [1, 0]]
        GameOfLife.solution(board)
        expected = [[1, 1], [1, 1]]
        self.assertEqual(
            expected,
            board,
        )


if __name__ == "__main__":
    unittest.main()
