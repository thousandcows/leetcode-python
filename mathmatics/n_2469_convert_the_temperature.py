from utils.time_measurement import time_measurement


class ConvertTheTemperature:
    @staticmethod
    @time_measurement
    def solution(celsius: float) -> list[float]:
        return [round(celsius + 273.15, 5), round(celsius * 1.80 + 32.00, 5)]
