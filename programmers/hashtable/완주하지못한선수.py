from collections import Counter

from utils.time_measurement import time_measurement


class UncompletedPlayer:
    @staticmethod
    @time_measurement
    def solution(participant: list[str], completion: list[str]) -> str:
        participant.sort()
        completion.sort()

        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]

        return participant[-1]

    @staticmethod
    @time_measurement
    def solution_with_counter(participant: list[str], completion: list[str]) -> str:
        return list((Counter(participant) - Counter(completion)).keys())[0]
