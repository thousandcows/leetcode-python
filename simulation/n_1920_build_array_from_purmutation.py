from utils.time_measurement import time_measurement


class BuildArrayFromPermutation:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]):
        return [nums[i] for i in nums]
