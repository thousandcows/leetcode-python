from itertools import combinations

from utils.time_measurement import time_measurement


class BinaryWatch:
    @staticmethod
    @time_measurement
    def solution(turned_on: int) -> list[str]:
        binary_watch = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        output = []

        for combi in combinations(range(len(binary_watch)), turned_on):
            time, hour, minute = "", 0, 0
            for index in combi:
                if index <= 3:
                    hour += binary_watch[index]
                else:
                    minute += binary_watch[index]
            if hour > 11 or minute > 59:
                continue
            colon = ":" if minute > 9 else ":0"
            output.append(f"{hour}:{minute:02d}")
        return output

    @staticmethod
    @time_measurement
    def backtrack_solution(turn_on: int) -> list[str]:
        def backtrack(count: int, hour: int, minute: int, start_idx: int):
            # Dead End
            if hour > 11 or minute > 59:
                return
            # Decision Point
            if count == turn_on:
                output.append(f"{hour}:{minute:02d}")

            # Backtrack
            for i in range(start_idx, 10):
                if i < 4:
                    backtrack(count + 1, hour + (1 << i), minute, i + 1)
                else:
                    backtrack(count + 1, hour, minute + (1 << i - 4), i + 1)

        output = []
        backtrack(0, 0, 0, 0)
        return output
