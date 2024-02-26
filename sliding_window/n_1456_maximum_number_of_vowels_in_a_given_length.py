from utils.time_measurement import time_measurement


class MaximumNumberOfVowelsInAGivenLength:
    @staticmethod
    @time_measurement
    def solution(s: str, k: int) -> int:
        ans = 0
        vowel = 'aeiou'
        for i in range(len(s) - k + 1):
            cnt = 0
            for char in s[i:i + k]:
                if char in vowel:
                    cnt += 1
            ans = max(cnt, ans)
            if ans == k:
                return k
        return ans
