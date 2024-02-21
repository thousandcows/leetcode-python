from utils.time_measurement import time_measurement


class MoveZeroes:
    @staticmethod
    @time_measurement
    def solution(nums):
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == 0:
                nums.remove(0)
                nums.append(0)
                right -= 1
                continue
            left += 1
        return nums
