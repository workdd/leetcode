class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0

        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            if grid[x][y] == "0":
                return

            grid[x][y] = "0"

            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt
