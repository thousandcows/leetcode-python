from utils.time_measurement import time_measurement


class IsSubsequence:
    @staticmethod
    @time_measurement
    def solution(s: str, t: str) -> bool:
        idx = 0
        t_idx = 0
        while idx < len(s) and t_idx < len(t):
            if s[idx] == t[t_idx]:
                idx += 1
                t_idx += 1
            else:
                t_idx += 1
        return idx == len(s)