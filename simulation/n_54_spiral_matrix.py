from utils.time_measurement import time_measurement


class SpiralMatrix:
    @staticmethod
    @time_measurement
    def solution(matrix: list[list[int]]) -> list[int]:
        row, col = len(matrix), len(matrix[0])
        visited = [[False for _ in range(col)] for _ in range(row)]

        visited[0][0] = True
        answer = [1]

        left, right = 0, 0
        for _ in range(row * col):
            while (
                0 <= left < row
                and 0 <= right + 1 < col
                and visited[left][right + 1] is False
            ):
                right += 1
                answer.append(matrix[left][right])
                visited[left][right] = True
            while (
                0 <= left + 1 < row
                and 0 <= right < col
                and visited[left + 1][right] is False
            ):
                left += 1
                answer.append(matrix[left][right])
                visited[left][right] = True
            while (
                0 <= left < row
                and 0 <= right - 1 < col
                and visited[left][right - 1] is False
            ):
                right -= 1
                answer.append(matrix[left][right])
                visited[left][right] = True
            while (
                0 <= left - 1 < row
                and 0 <= right < col
                and visited[left - 1][right] is False
            ):
                left -= 1
                answer.append(matrix[left][right])
                visited[left][right] = True
        return answer
