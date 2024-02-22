from utils.time_measurement import time_measurement


class ContainerWithMostWater:
    @staticmethod
    @time_measurement
    def solution(height: list[int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0
        while left < right:
            volume = (right - left) * min(height[left], height[right])
            answer = max(volume, answer)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return answer
