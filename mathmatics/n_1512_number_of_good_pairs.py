from collections import Counter
from itertools import combinations

from utils.time_measurement import time_measurement


class NumberOfGoodPairs:
    @staticmethod
    @time_measurement
    def solution(nums: list[int]) -> int:
        count_dict = Counter(nums)
        answer = 0
        for key, count in count_dict.items():
            if count >= 2:
                answer += len(list(combinations(range(count), 2)))
        return answer
