from collections import Counter

from utils.time_measurement import time_measurement


class Pokemon:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        return min(len(Counter(nums)), len(nums) // 2)
