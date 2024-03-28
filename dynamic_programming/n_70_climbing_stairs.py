from utils.time_measurement import time_measurement


class ClimbingStairs:
    @staticmethod
    @time_measurement
    def solution(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
