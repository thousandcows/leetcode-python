from utils.time_measurement import time_measurement


class SlidingWindowMaximum:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], k: int) -> list[int]:
        results = []
        for i in range(len(nums) - k + 1):
            results.append(max(nums[i:i + k]))
        return results
