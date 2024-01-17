from utils.time_measurement import time_measurement


class ValidParentheses:
    @staticmethod
    @time_measurement
    def solution(s: str) -> bool:
        stack = []
        parentheses_dict = {
            "]": "[",
            ")": "(",
            "}": "{",
        }
        for char in s:
            if char not in parentheses_dict:
                stack.append(char)
                continue

            if not stack or stack.pop() != parentheses_dict[char]:
                return False
        return len(stack) == 0
