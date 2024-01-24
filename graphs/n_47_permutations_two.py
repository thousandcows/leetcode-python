from itertools import permutations

from utils.time_measurement import time_measurement


class PermutationsTwo:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> list[list[int]]:
        return list(map(list, set(permutations(nums, len(nums)))))
