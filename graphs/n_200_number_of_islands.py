from utils.time_measurement import time_measurement


class NumberOfIslands:
    def dfs(self, grid: list[list[str]], row: int, col: int) -> None:
        if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
            return

        if grid[row][col] != "1":
            return

        grid[row][col] = 0

        self.dfs(grid, row + 1, col)
        self.dfs(grid, row + -1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col + -1)

    @time_measurement
    def solution(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    count += 1

        return count
