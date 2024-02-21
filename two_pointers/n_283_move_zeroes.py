from utils.time_measurement import time_measurement


class MoveZeroes:
    @staticmethod
    @time_measurement
    def solution(nums):
        zero_idx, non_zero_idx = 0, 0
        count_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            else:
                nums[non_zero_idx] = nums[i]
                non_zero_idx += 1

        for i in range(len(nums) - 1, len(nums) - count_zero - 1, -1):
            nums[i] = 0

        return nums

