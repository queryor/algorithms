# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

# Example 1:

# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Example 2:

# Input: s1 = "abcde", s2 = "caebd"
# Output: false
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        ## 超时
        if len(s1)!=len(s2):
            return False
        n = len(s1)
        if n ==0:
            return True
        if n ==1:
            if s1[0]==s2[0]:
                return True
            else: 
                return False
        else: 
            ans = False
            for m in range(1,n):
                #print(m)
                ans = (self.isScramble(s1[:m],s2[:m]) and self.isScramble(s1[m:],s2[m:])) or (self.isScramble(s1[:m],s2[-m:]) and self.isScramble(s1[m:],s2[:-m]))
                #print(ans)
                if ans == True:
                    break
            return ans
    def isScramble1(self, s1: str, s2: str) -> bool:
        # dp 三维 
        # dp[i][j][n]，其中i是s1的起始字符，j是s2的起始字符，而n是当前的字符串长度
        if len(s1)!=len(s2):
            return False
        n = len(s1)
        if s1 == s2:
            return True
        dp = [[[False for i in range(n+1)] for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i]==s2[j]
        for l in range(2,n+1):
            for i in range(n-l+1):
                for j in range(n-l+1):
                    for k in range(1,l):
                        if dp[i][j][k] and dp[i+k][j+k][l-k] or dp[i+k][j][l-k] and dp[i][j+l-k][k]:
                            dp[i][j][l]=True
        return dp[0][0][n]

s = Solution()
s1 = 'ab'
s2 = 'baa'
print(s.isScramble1(s1,s2))