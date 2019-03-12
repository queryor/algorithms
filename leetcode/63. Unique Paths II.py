# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        # Runtime: 40 ms, faster than 59.37% of Python3 online submissions for Unique Paths II.
        # Memory Usage: 12.9 MB, less than 5.19% of Python3 online submissions for Unique Paths II.
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        dp[1][1] = int(1 and not obstacleGrid[0][0])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i ==j and i==1:
                    continue
                if obstacleGrid[i-1][j-1]==0:
                    dp[i][j]=(dp[i-1][j]+dp[i][j-1])
                else: 
                    dp[i][j]=0
        #print(dp)
        return dp[m][n]

s = Solution()
i = [[0,0]]
print(s.uniquePathsWithObstacles(i))