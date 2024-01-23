from itertools import combinations

from utils.time_measurement import time_measurement


class Combinations:
    @staticmethod
    @time_measurement
    def solution_combinations(n: int, k: int) -> list:
        return list(map(list, combinations([i for i in range(1, n + 1)], k)))

    @staticmethod
    @time_measurement
    def solution_dfs(n: int, k: int) -> list:
        def dfs(elements: list[int], start: int, count_down: int):
            if count_down == 0:
                result.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, count_down - 1)
                elements.pop()

        result = []
        dfs([], 1, k)
        return result
