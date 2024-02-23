
from utils.time_measurement import time_measurement
from collections import deque

class SlidingWindowMaximum:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []

        window = deque()
        result = []

        for i, n in enumerate(nums):

            while window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[window[-1]] < n:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result
