from utils.time_measurement import time_measurement


class CountOfMatchesInTournament:
    @staticmethod
    @time_measurement
    def solution(n: int) -> int:
        return n - 1
