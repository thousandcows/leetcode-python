from utils.time_measurement import time_measurement


class FindTheHighestAltitude:
    @staticmethod
    @time_measurement
    def solution(gain: list[int]) -> int:
        current_altitude = highest_altitude = 0

        for g in gain:
            current_altitude += g
            highest_altitude = max(highest_altitude, current_altitude)

        return highest_altitude
