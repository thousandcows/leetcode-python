from utils.time_measurement import time_measurement


class JewelsAndStones:
    @staticmethod
    @time_measurement
    def solution(jewels: str, stones: str) -> int:
        hash = {}
        for j in jewels:
            hash[j] = True
        counter = 0
        for s in stones:
            if s in hash:
                counter += 1
        return counter
