from utils.time_measurement import time_measurement


class MaxConsecutiveOnes:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # Flip the bit from 0 to 1
            k -= 1 - nums[right]
            # If there are more than k 0's, move the left pointer and undo the flip
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return len(nums) - left
