# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
class Solution:
    def __init__(self):
        self.cache = {}
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if len(p)==0:
            return len(s)==0
        question = s +"+"+p
        if question in self.cache:
            return self.cache[question]
        if p[0]=='*':
            if len(s)==0:
                res = self.isMatch(s,p[1:])
            else:
                res = self.isMatch(s[1:],p) or self.isMatch(s[1:],p[1:]) or self.isMatch(s,p[1:])
        elif len(s)==0:
            res=False
        elif p[0]==s[0] or p[0]=='?':
            res = self.isMatch(s[1:],p[1:])
        else:
            res=False
        self.cache[question]=res
        #print(self.cache)
        return res
    def isMatch1(self,s,p):
        dp = [[False for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for i in range(len(s)+1):
            for j in range(1,len(p)+1):
                if(p[j-1]=='*'):
                    dp[i][j]=dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
                else: 
                    dp[i][j]=dp[i-1][j-1] and i>0 and (s[i-1] == p[j-1] or p[j-1]=='?')
        return dp[len(s)][len(p)]

s  = Solution()
a = "babb"
p = "*b*b"
print(s.isMatch(a,p))