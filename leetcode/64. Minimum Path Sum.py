# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution:
    def minPathSum(self, grid) -> int:
        ## 用dp[i][j]表示到i,j点的最短距离

        # Runtime: 56 ms, faster than 64.99% of Python3 online submissions for Minimum Path Sum.
        # Memory Usage: 14.6 MB, less than 9.86% of Python3 online submissions for Minimum Path Sum.

        m = len(grid)
        n = len(grid[0])
        k = 2**31
        dp = [[k for i in range(n+1)] for i in range(m+1)]
        dp[1][1] = grid[0][0]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i ==j and i==1:
                    continue
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
        #print(dp)
        return dp[m][n]
        