from itertools import permutations

from utils.time_measurement import time_measurement


class FindPrimeNumber:

    @staticmethod
    @time_measurement
    def solution(numbers: str) -> int:
        answer_set = set()

        for i in range(len(numbers)):
            answer_set |= set(map(int, map("".join, permutations(numbers, i + 1))))

        answer_set -= set(range(0, 2))
        for i in range(2, int(max(answer_set) ** 0.5) + 1):
            answer_set -= set(range(i * 2, max(answer_set) + 1, i))

        return len(answer_set)
