from utils.time_measurement import time_measurement


class FinalValueOfVariableAfterPerformingOperations:
    @staticmethod
    @time_measurement
    def solution(operations: list[str]) -> int:
        return sum([1 if "+" in op else -1 for op in operations])
