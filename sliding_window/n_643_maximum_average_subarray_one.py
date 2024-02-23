import math

from utils.time_measurement import time_measurement


class MaximumAverageSubarrayOne:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], k: int) -> float:
        window_sum = sum(nums[:k])
        answer = window_sum
        for i in range(1, len(nums) - k + 1):
            window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
            answer = max(answer, window_sum)
        return round(answer / k, 5)