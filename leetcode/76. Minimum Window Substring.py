# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ## 滑动窗口思想
        # 参考 http://www.cnblogs.com/grandyang/p/4340948.html
        res = ""
        letterCnt = {}
        left = 0
        cnt = 0
        minLen = 2**31
        for c in t :
            if c in letterCnt:
                letterCnt[c]+=1
            else:
                letterCnt[c]=1
        for i in range(len(s)):
            if s[i] in letterCnt:
                letterCnt[s[i]]-=1
                if letterCnt[s[i]]>=0:
                    cnt+=1
            while cnt == len(t):
                if minLen>i-left+1:
                    minLen = i-left+1
                    res = s[left:left+minLen]
                if s[left] in letterCnt:
                    letterCnt[s[left]]+=1
                    if letterCnt[s[left]]>0:
                        cnt-=1
                left+=1
        return res


so = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(so.minWindow(S,T))