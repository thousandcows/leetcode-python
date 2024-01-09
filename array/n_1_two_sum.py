from utils.time_measurement import time_measurement


class TwoSome:
    @staticmethod
    @time_measurement
    def execute(nums: list[int], target: int) -> list[int]:
        for idx, num in enumerate(nums):
            pair_number = target - num
            if pair_number in nums[idx + 1 :]:
                return [idx, nums[idx + 1 :].index(pair_number) + idx + 1]
