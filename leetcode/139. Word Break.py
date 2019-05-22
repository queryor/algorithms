'''Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        ## dfs memo存中间结果
        Wordset = set(wordDict)
        memo = [-1 for i in range(len(s))]
        return self.dfs(s,0,Wordset,memo)
    def dfs(self,s,id,Wordset,memo):
        if id >= len(s):
            return True
        if memo[id]!=-1:
            return memo[id]
        for endid in range(id,len(s)):
            if s[id:endid+1] in Wordset:
                if self.dfs(s,endid+1,Wordset,memo):
                    memo[id] = True
                    return memo[id]
        memo[id]= False
        return memo[id]
    def wordBreak1(self, s: str, wordDict) -> bool:
        #dp
        Wordset = set(wordDict)
        dp = [False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(s)+1):
            #print(str(i)+":",end=' ')
            for j in range(i):
                #print(s[j:i])
                if dp[j] and s[j:i] in Wordset:
                    dp[i] = True
                    break
        #print(dp)
        return dp[-1]
s = Solution()
i = "goalspecial"
wordDict = ["go","goal","goals","special"]
print(s.wordBreak1(i,wordDict))