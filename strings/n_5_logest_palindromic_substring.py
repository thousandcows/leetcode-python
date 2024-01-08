from utils.time_measurement import time_measurement


class LongestPalindromicSubstring:
    @staticmethod
    @time_measurement
    def execute(s: str) -> str:
        # Define method
        def expand_pointers(start: int, end: int) -> str:
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start + 1: end]

        # Exception handling
        if len(s) < 2 or s == s[::-1]:
            return s

        # Start slicing from the middle of the string
        answer = ""
        for i in range(len(s) - 1):
            answer = max(
                answer, expand_pointers(i, i + 1), expand_pointers(i, i + 2), key=len
            )

        return answer
