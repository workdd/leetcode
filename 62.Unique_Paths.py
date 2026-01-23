class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * 100 for _ in range(100)]

        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                print(row, col)
                if row == 0 and col == 0:
                    continue
                if row == 0:
                    dp[row][col] = dp[row][col - 1]
                elif col == 0:
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row][col - 1] + dp[row - 1][col]
        return dp[m - 1][n - 1]
