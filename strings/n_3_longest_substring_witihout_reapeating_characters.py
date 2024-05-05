from utils.time_measurement import time_measurement


class LongestSubstringWithoutRepeatingCharacters:
    @staticmethod
    @time_measurement
    def solution(s: str) -> int:
        answer, start_index = 0, 0
        visited = {}
        for idx, char in enumerate(s):
            if char in visited and start_index <= visited[char]:
                start_index = visited[char] + 1
            else:
                answer = max(answer, idx - start_index + 1)
            visited[char] = idx
        return answer
