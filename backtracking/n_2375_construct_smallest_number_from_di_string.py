from itertools import permutations

from utils.time_measurement import time_measurement


class ConstructSmallestNumberFromDIString:
    @staticmethod
    @time_measurement
    def bruteforce_solution(pattern: str) -> str:
        num_list = [str(i) for i in range(1, len(pattern) + 2)]
        possible_strings = list(map(lambda x: "".join(x), permutations(num_list)))

        for st in possible_strings:
            flag = True
            for i, p in enumerate(pattern):
                if (p == "D" and st[i] < st[i + 1]) or (p == "I" and st[i] > st[i + 1]):
                    flag = False
                    break
            if flag:
                return st
