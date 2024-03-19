from utils.time_measurement import time_measurement


class SumOfAllSubsetXORTotals:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        def backtrack(count: int, limit: int, curr_sum: int, curr_idx: int):
            nonlocal total
            curr_sum = curr_sum ^ nums[curr_idx]

            if count == limit:
                total += curr_sum
                return

            for idx in range(curr_idx + 1, len(nums)):
                backtrack(count + 1, limit, curr_sum, idx)

        total = 0
        for limit in range(1, len(nums) + 1):
            for start_idx in range(len(nums)):
                backtrack(1, limit, 0, start_idx)
        return total

    @staticmethod
    @time_measurement
    def bitwise_solution(nums: list[int]) -> int:
        bits = 0
        for n in nums:
            bits |= n
            print(bits)
        return bits * 2 ** (len(nums) - 1)
