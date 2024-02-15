from utils.time_measurement import time_measurement


class ReverseWordsInAString:
    @staticmethod
    @time_measurement
    def solution(s: str) -> str:
        return " ".join((s.split())[::-1])
