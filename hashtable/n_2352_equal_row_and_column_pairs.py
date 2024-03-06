from collections import Counter

from utils.time_measurement import time_measurement


class EqualRowAndColumnPairs:

    @staticmethod
    @time_measurement
    def solution_two(grid: list[list[int]]) -> int:
        row = Counter(map(tuple, grid))
        col = Counter(zip(*grid))
        return sum(row.get(t, 0) * col.get(t, 0) for t in row)

    @staticmethod
    @time_measurement
    def solution(grid: list[list[int]]) -> int:
        row_dict = {i: [] for i in range(len(grid))}

        for row in grid:
            for i, v in enumerate(row):
                row_dict[i].append(v)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if row_dict[i] == grid[j]:
                    cnt += 1

        return cnt
