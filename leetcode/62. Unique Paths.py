# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Note: m and n will be at most 100.


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 超时  因为是一层一层遍历下去的。可以用动态规划的思想存一下中间结果
        if m==0 or n==0:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
    def uniquePaths1(self, m: int, n: int) -> int:
        # 动态规划
        # Runtime: 40 ms, faster than 42.86% of Python3 online submissions for Unique Paths.
        # Memory Usage: 13.1 MB, less than 5.25% of Python3 online submissions for Unique Paths.

        # 其实这个还可以根据 dp[m][n]=dp[n][m]再优化一下
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(n+1):
            dp[1][i] = 1
        for i in range(m+1):
            dp[i][1] = 1
        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m][n]
                    
    def uniquePaths2(self,m,n):
        ## 根据 dp[m][n]=dp[n][m]优化成功 
        # Runtime: 36 ms, faster than 73.35% of Python3 online submissions for Unique Paths.
        # Memory Usage: 13.2 MB, less than 5.25% of Python3 online submissions for Unique Paths.
        m,n = min(m,n),max(m,n)
        dp = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(n+1):
            dp[1][i] = 1
        for i in range(m+1):
            dp[i][1] = 1
        for i in range(2,m+1):
            for j in range(i,n+1):
                if j != i:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
                else: 
                    dp[i][j]=dp[i-1][j]+dp[j-1][i]      
        return dp[m][n]

s = Solution()
print(s.uniquePaths2(7,3))