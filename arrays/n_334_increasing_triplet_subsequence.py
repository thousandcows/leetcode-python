import math

from utils.time_measurement import time_measurement


class IncreasingTripletSubsequence:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = math.inf
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                print(f"first: {first}, second: {second}, n: {n}")
                return True
        return False
