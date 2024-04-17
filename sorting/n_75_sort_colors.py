from utils.time_measurement import time_measurement


class SortColors:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp

        return nums
