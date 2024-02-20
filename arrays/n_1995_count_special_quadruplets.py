from itertools import combinations

from utils.time_measurement import time_measurement


class CountSpecialQuadruplets:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        if len(nums) < 4:
            return 0

        ans = 0
        for combi in combinations(nums, 4):
            if combi[0] + combi[1] + combi[2] == combi[3]:
                ans += 1

        return ans
