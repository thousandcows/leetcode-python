from itertools import permutations

from utils.time_measurement import time_measurement


class LetterTilePossibilities:
    @staticmethod
    @time_measurement
    def solution(tiles: str) -> int:
        answer = 0
        for i in range(1, len(tiles) + 1):
            answer += len(set(permutations(tiles, i)))
        return answer
