from utils.time_measurement import time_measurement


class RearrangeArrayElementsBySign:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> list[int]:
        ans = [0 for _ in range(len(nums))]
        positive_idx, negative_idx = 0, 1
        for i, num in enumerate(nums):
            if num > 0:
                ans[positive_idx] = num
                positive_idx += 2
            else:
                ans[negative_idx] = num
                negative_idx += 2
        return ans
