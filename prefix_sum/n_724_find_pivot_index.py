from utils.time_measurement import time_measurement


class FindPivotIndex:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        total = sum(nums)
        left_sum, right_sum = 0, total

        # Return 0 if the first element is the pivot
        if left_sum == right_sum - nums[0]:
            return 0

        # Iterate indexes and return if it's the pivot
        right_sum -= nums[0]
        for i in range(1, len(nums) - 1):

            left_sum += nums[i - 1]
            right_sum -= nums[i]

            if left_sum == right_sum:
                return i

        # Return the last element if it's the pivot
        if total - nums[-1] == 0:
            return len(nums) - 1

        # Return -1 if there's no pivot
        return -1
