from collections import Counter

from utils.time_measurement import time_measurement


class JewelsAndStones:
    @staticmethod
    @time_measurement
    def solution(jewels: str, stones: str) -> int:
        return sum(Counter(stones)[j] for j in jewels)
