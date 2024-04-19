from utils.time_measurement import time_measurement


class MinimumNumberGame:
    @staticmethod
    @time_measurement
    def solution_with_list_func(nums: list[int]) -> list[int]:
        arr = []
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            arr.extend([nums[i + 1], nums[i]])
        return arr

    @staticmethod
    @time_measurement
    def solution_with_swaps(nums: list[int]) -> list[int]:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
