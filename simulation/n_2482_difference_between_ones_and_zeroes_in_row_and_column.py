from utils.time_measurement import time_measurement


class DifferenceBetweenOnesAndZerosInRowAndColumn:
    @staticmethod
    @time_measurement
    def solution(grid: list[list[int]]):
        row_len = len(grid)
        col_len = len(grid[0])

        ones_row = [row.count(1) for row in grid]
        ones_col = [sum(col) for col in zip(*grid)]

        return [
            [
                2 * ones_row[r] + 2 * ones_col[c] - row_len - col_len
                for c in range(col_len)
            ]
            for r in range(row_len)
        ]
