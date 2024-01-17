from utils.time_measurement import time_measurement


class DailyTemperatures:
    @staticmethod
    @time_measurement
    def solution(temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        return ans
