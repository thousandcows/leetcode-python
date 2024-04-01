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

    @staticmethod
    @time_measurement
    def backtracking_solution(pattern: str) -> str:
        def backtrack(curr_num: int, curr_idx: int, used: set, last_digit: int):
            nonlocal min_str

            if str(curr_num) > str(min_str):
                return

            if len(used) == len(pattern) + 1:
                min_str = min(min_str, curr_num)
                return

            for n in num_list:
                if n in used:
                    continue
                if pattern[curr_idx] == "D" and n > last_digit:
                    continue
                if pattern[curr_idx] == "I" and n < last_digit:
                    continue
                backtrack(curr_num * 10 + n, curr_idx + 1, used | {n}, n)

        min_str = float("inf")
        num_list = [i for i in range(1, len(pattern) + 2)]
        for n in num_list:
            backtrack(n, 0, {n}, n)

        return str(min_str)
