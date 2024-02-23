import math

from utils.time_measurement import time_measurement


class MaximumAverageSubarrayOne:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], k: int) -> float:
        answer = -math.inf
        for i in range(len(nums) - k + 1):
            answer = max(answer, sum(nums[i:i + k]))
        return round(answer / k, 5)