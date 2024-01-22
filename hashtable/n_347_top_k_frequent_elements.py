from collections import Counter

from utils.time_measurement import time_measurement


class TopKFrequentElements:
    @staticmethod
    @time_measurement
    def solution(nums: list, k: int) -> list:
        return list(zip(*Counter(nums).most_common(k)))[0]
