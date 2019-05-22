"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
class Solution:
    def wordBreak(self, s: str, wordDict):
        #dfs 超时
        Wordset = set(wordDict)
        ans = []
        self.dfs(s,0,Wordset,ans)
        return ans
    
    def dfs(self,s,start,Wordset,ans,res=""):
        if start>=len(s):
            ans.append(res)
            return
        for i in range(start,len(s)):
            if s[start:i+1] in Wordset:
                p_res = res
                res+=s[start:i+1] if len(res)==0 else " "+s[start:i+1]
                self.dfs(s,i+1,Wordset,ans,res)
                res = p_res 
        #print(res)
    def wordBreak1(self, s: str, wordDict):
        #dp 	Memory Limit Exceeded
        dp = [False for i in range(len(s)+1)]
        dp_res = [[] for i in range(len(s)+1)]
        Wordset = set(wordDict)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in Wordset:
                    dp[i] = True
                    if j == 0:
                        dp_res[i].append(s[j:i])
                    else:
                        for res in dp_res[j]:
                            dp_res[i].append(res+" "+s[j:i])
        #print(dp_res)
        return dp_res[-1]

    def wordBreak2(self, s: str, wordDict):
        ## 用一个中间hashmap 记录中间结果
        m = {}
        return self.dfs2(s,wordDict,m)
    def dfs2(self,s,wordDict,m):
        if s in m:
            return m[s]
        if len(s)==0:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)]!=word:
                continue
            rem = self.dfs2(s[len(word):],wordDict,m)
            for str_t in rem:
                res.append(word+("" if len(str_t)==0 else " ")+ str_t)
        m[s]=res
        #print(res)
        return m[s]
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]      
so = Solution()
print(so.wordBreak2(s,wordDict))