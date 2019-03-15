# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
class Solution:
    def numDecodings(self, s: str) -> int:
        ##dp
        ### 主要是要处理好各种情况的转移方程
        n = len(s)
        if n==0:
            return n
        dp = [1 for i in range(n+1)]
        dp[1] = 0 if int(s[0])==0 else 1
        for i in range(2,n+1):
            pre_num = int(s[i-2])
            cur_num = int(s[i-1])
            if cur_num == 0 and pre_num ==0:
                dp[i]=0
            elif cur_num==0:
                if pre_num<=2:
                    dp[i]=dp[i-2]
                else: 
                    dp[i]=0
            elif pre_num == 0 :
                dp[i]=dp[i-1]
            elif pre_num*10+cur_num <=26:
                dp[i]=dp[i-1]+dp[i-2]
            else: 
                dp[i]=dp[i-1]
            
        return dp[n]
