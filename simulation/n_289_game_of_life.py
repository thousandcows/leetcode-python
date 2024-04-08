from utils.time_measurement import time_measurement


class GameOfLife:
    @staticmethod
    @time_measurement
    def solution(board: list[list[int]]):
        m = len(board)
        n = len(board[0])

        matrix_counter = [[0 for _ in range(n)] for _ in range(m)]

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
        ]

        for row in range(m):
            for col in range(n):
                count = 0
                for d in directions:
                    nx = row + d[0]
                    ny = col + d[1]

                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 1:
                        count += 1
                matrix_counter[row][col] = count
        for row in range(m):
            for col in range(n):
                if board[row][col] == 0 and matrix_counter[row][col] == 3:
                    board[row][col] = 1
                elif board[row][col] == 1 and matrix_counter[row][col] not in (2, 3):
                    board[row][col] = 0
