'''Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
# dp。设dp[i]为[0,i]这个闭区间上的最少切割数。

# dp[i]=0 如果[o,i]为回文串
# dp[i] = min(dp[j-1]+1,dp[i]) ([j,i] 是回文串 1<=j<=i)

# 我们枚举k为当前计算的位置，然后用双指针的思想，从k向两边扩散，
# 判断是否回文（要分别计算长度为奇数和偶数的情况），并根据上述公式更新dp数组。这样，就可以将第一种解法的枚举j和判断回文合并起来，从而把复杂度降低为O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        def helper(i, j):
            while j >= 0 and i < n:
                if s[i] != s[j]: break
                dp[i] = min(dp[i], dp[j - 1] + 1 if j > 0 else 0)
                i, j = i + 1, j - 1

        n = len(s)
        dp = [i for i in range(n)]
        for k in range(1, n):
            helper(k, k)  # odd case
            helper(k, k - 1)  # even case
        return dp[n - 1]