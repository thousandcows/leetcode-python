from collections import defaultdict

from utils.time_measurement import time_measurement


class CountNumberOfMaximumBitwiseOrSubsets:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        def dfs(last_value: int, curr_index):
            nonlocal max_val, max_count, end

            curr_value = last_value | nums[curr_index]
            if curr_value == max_val:
                max_count += 1
            elif curr_value > max_val:
                max_val = curr_value
                max_count = 1

            for idx in range(curr_index + 1, end):
                dfs(curr_value, idx)

        max_val = -1
        max_count = 0
        end = len(nums)
        for start_index in range(end):
            dfs(0, start_index)

        return max_count

    @staticmethod
    @time_measurement
    def solution_dp(nums: list[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            for key, value in list(dp.items()):
                dp[key | num] += value
        return dp[max(dp.keys())]
