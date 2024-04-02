from utils.time_measurement import time_measurement


class FindGreatestCommonDivisorOfArray:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        while max_num % min_num != 0:
            max_num, min_num = min_num, max_num % min_num
        return min_num
