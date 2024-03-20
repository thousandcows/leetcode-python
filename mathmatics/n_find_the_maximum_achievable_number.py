from utils.time_measurement import time_measurement


class FindTheMaximumAchievableNumber:
    @staticmethod
    @time_measurement
    def solution(num: int, t: int) -> int:
        return num + (t << 1)
