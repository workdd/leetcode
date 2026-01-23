class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_cnt = 0

        def dfs(x, y):
            nonlocal cnt
            if x < 0 or y < 0 or x >= rows or y >= cols:
                return
            if grid[x][y] == 0:
                return

            grid[x][y] = 0
            cnt += 1

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    cnt = 0
                    dfs(i, j)
                    max_cnt = max(max_cnt, cnt)

        return max_cnt
