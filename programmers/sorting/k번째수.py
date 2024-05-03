from utils.time_measurement import time_measurement


class KthNumber:
    @staticmethod
    @time_measurement
    def solution(array: list[int], commands: list[list[int]]) -> list[int]:
        return [
            sorted(n for i, n in enumerate(array) if command[0] - 1 <= i < command[1])[
                command[2] - 1
            ]
            for command in commands
        ]
