from utils.time_measurement import time_measurement


class LongestSubstringWithoutRepeatingCharacters:
    @staticmethod
    @time_measurement
    def solution(s: str) -> int:
        if len(s) <= 1:
            return len(s)

        answer, left, right = 0, 0, 0
        curr_substr_set = set()

        while right < len(s):
            if left == right:
                curr_substr_set.add(s[left])
                right += 1
            elif left < right:
                if s[right] not in curr_substr_set:
                    curr_substr_set.add(s[right])
                    right += 1
                else:
                    left += 1
                    right = left
                    curr_substr_set = set(s[left])
            answer = max(answer, right - left)
        return answer
