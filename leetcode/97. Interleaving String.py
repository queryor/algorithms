# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Example 1:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#   只要是遇到字符串的子序列或是匹配问题直接就上动态规划Dynamic Programming，其他的都不要考虑
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 16%
        if len(s1)+len(s2)!=len(s3):
            return False
        n1 = len(s1)
        n2 = len(s2)
        dp = [[0 for i in range(n2+1)]for i in range(n1+1)]
        dp[0][0]=True
        #s2 为空
        for i in range(1,n1+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        # s1 为空
        for i in range(1,n2+1):
            dp[0][i]=dp[0][i-1] and s2[i-1]==s3[i-1]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                dp[i][j]=((dp[i-1][j]) and s1[i-1]==s3[i-1+j]) \
                     or (dp[i][j-1] and s2[j-1]==s3[j-1+i])
        return dp[n1][n2]       

    ### DFS 和 BFS 解法未解决