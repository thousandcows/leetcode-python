from utils.time_measurement import time_measurement


class NumberOfIslands:
    @staticmethod
    @time_measurement
    def solution(grid: list[list[str]]) -> int:
        length = len(grid)
        width = len(grid[0])
        visited = [[False] * width] * length
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(row: int, col: int, visited: list[list[bool]]):
            visited[row][col] = True
            for di in direction:
                n_row, n_col = row + di[0], col + di[1]

                if 0 <= n_row < length and 0 <= n_col < width:
                    if grid[n_row][n_col] == "1" and not visited[n_row][n_col]:
                        bfs(n_row, n_col, visited)

        count = 0

        for r in range(length):
            for c in range(width):
                if grid[r][c] == "1" and visited[r][c] is False:
                    print(f"r: {r}, c: {c}")
                    bfs(r, c, visited)
                    count += 1

        return count
