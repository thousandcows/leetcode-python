from utils.time_measurement import time_measurement


class NumberOfIslands:
    @time_measurement
    def solution(self, grid: list[list[str]]) -> int:
        def dfs(row: int, col: int) -> None:
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
                return

            if grid[row][col] != "1":
                return

            grid[row][col] = 0

            dfs(row + 1, col)
            dfs(row + -1, col)
            dfs(row, col + 1)
            dfs(row, col + -1)

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count
