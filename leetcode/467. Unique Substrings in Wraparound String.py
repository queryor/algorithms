# Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

# Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

# Note: p consists of only lowercase English letters and the size of p might be over 10000.

# Example 1:
# Input: "a"
# Output: 1

# Explanation: Only the substring "a" of string "a" is in the string s.
# Example 2:
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string s.
# Example 3:
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        #   只要是遇到字符串的子序列或是匹配问题直接就上动态规划Dynamic Programming，其他的都不要考虑!!!!
        ## dp[i] 表示以字符串p[i]结尾的最长顺序字符串的长度
        n = len(p)
        if n<=1:
            return n
        dp = [0 for i in range(n+1)]
        dp[0]=0
        cnt = [0 for i in range(26)]
        for i in range(1,n+1):
            if i>1 and (ord(p[i-1])==ord(p[i-2])+1 or ord(p[i-2])-ord(p[i-1])==25):
                dp[i]=dp[i-1]+1
            else:
                dp[i]=1
            cnt[ord(p[i-1])-ord('a')] = max(cnt[ord(p[i-1])-ord('a')],dp[i]) 
        # print(dp)
        # print(cnt)
        return sum(cnt)
s = Solution()
i = "zab"
print(s.findSubstringInWraproundString(i))