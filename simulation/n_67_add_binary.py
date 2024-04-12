from utils.time_measurement import time_measurement


class AddBinary:
    @staticmethod
    @time_measurement
    def solution(a: str, b: str):
        return bin(int(a, 2) + int(b, 2))[2:]
