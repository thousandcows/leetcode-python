from utils.time_measurement import time_measurement


class CreateTargetArrayInTheGivenOrder:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], index: list[int]):
        target_array = []
        for idx, value in zip(index, nums):
            target_array.insert(idx, value)
        return target_array
