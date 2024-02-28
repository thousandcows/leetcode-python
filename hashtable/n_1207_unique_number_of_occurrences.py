from collections import Counter

from utils.time_measurement import time_measurement


class UniqueNumberOfOccurrences:
    @staticmethod
    @time_measurement
    def solution(arr: list[int]) -> bool:
        return len(arr) == sum(set(Counter(arr).values()))
