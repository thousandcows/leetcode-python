from utils.time_measurement import time_measurement


class MaximumNumberOfVowelsInAGivenLength:
    @staticmethod
    @time_measurement
    def solution(s: str, k: int) -> int:
        vowels = 'aeiou'
        cnt = sum(s[i] in vowels for i in range(k))
        ans = cnt
        for i in range(k, len(s)):

            if s[i] in vowels:
                cnt += 1

            if s[i - k] in vowels:
                cnt -= 1

            ans = max(ans, cnt)

            if ans == k: return k

        return ans
