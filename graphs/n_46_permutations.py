from itertools import permutations

from utils.time_measurement import time_measurement


class Permutations:
    @staticmethod
    @time_measurement
    def solution(nums: list) -> list[list[int]]:
        return list(map(list, permutations(nums, len(nums))))
