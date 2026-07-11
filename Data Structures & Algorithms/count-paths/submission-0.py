class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Subproblems: The number of unique paths at at part of the maze grid[i][j], where i>m and j>n. Final result = grid[m-1][n-1]
        # Reccurence: OPT(i,j) = OPT([i-1][j]) + OPT([j-1][i]). Base case = OPT(0,0) = 0, OPT(m,0) = 1, OPT(0,n) = 1
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        dp[0][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

        