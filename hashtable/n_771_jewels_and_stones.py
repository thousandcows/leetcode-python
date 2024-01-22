from utils.time_measurement import time_measurement


class JewelsAndStones:
    @staticmethod
    @time_measurement
    def solution(jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
