class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a DP table with all elements set to 0
        dp = [[0] * n for _ in range(m)]
        
        # Fill the first row and first column with 1s (only one way to reach these cells)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        # Fill the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right corner contains the total unique paths
        return dp[m - 1][n - 1]
