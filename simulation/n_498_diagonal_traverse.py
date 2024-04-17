from utils.time_measurement import time_measurement


class DiagonalTraverse:
    @staticmethod
    @time_measurement
    def solution(mat: list[list[int]]) -> list[int]:
        ans = [mat[0][0]]
        row, col = 0, 0
        m, n = len(mat), len(mat[0])

        while not (row == m - 1 and col == n - 1):
            if 0 <= row < m and 0 <= col + 1 < n:
                col += 1
            elif 0 <= row + 1 < m and 0 <= col < n:
                row += 1
            else:
                continue

            while True:
                ans.append(mat[row][col])

                if row + 1 >= m or col - 1 < 0:
                    break

                row += 1
                col -= 1

            if 0 <= row + 1 < m and 0 <= col < n:
                row += 1
            elif 0 <= row < m and 0 <= col + 1 < n:
                col += 1
            else:
                continue

            while True:
                ans.append(mat[row][col])

                if col + 1 >= n or row - 1 < 0:
                    break

                row -= 1
                col += 1
        return ans
