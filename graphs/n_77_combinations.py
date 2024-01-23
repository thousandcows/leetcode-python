from itertools import combinations

from utils.time_measurement import time_measurement


class Combinations:
    @staticmethod
    @time_measurement
    def solution(n: int, k: int) -> list:
        return list(map(list, combinations([i for i in range(1, n + 1)], k)))
