from utils.time_measurement import time_measurement


class ConcatenationOfArray:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> list[int]:
        return nums * 2
