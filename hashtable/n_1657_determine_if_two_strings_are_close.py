from collections import Counter

from utils.time_measurement import time_measurement


class DetermineIfTwoStringsAreClose:
    @staticmethod
    @time_measurement
    def solution(word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        if word1 == word2:
            return True

        dict_one = Counter(word1)
        dict_two = Counter(word2)

        return sorted(dict_one.values()) == sorted(dict_two.values())
