from itertools import combinations

from utils.time_measurement import time_measurement


class CountPairsWhoseSumIsLessThanTarget:
    @staticmethod
    @time_measurement
    def solution(nums: list[int], target: int) -> int:
        count = 0
        for combi in combinations(nums, 2):
            if sum(combi) < target:
                count += 1

        return count
