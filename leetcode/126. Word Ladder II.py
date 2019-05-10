# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: []

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        # 超时
        ans = []
        if wordList == [] or endWord not in wordList:
            return ans
        self.min = 0x7ffffff
        self.dfs(beginWord,endWord,wordList,ans,[])
        #print(self.min)
        # 去除长的res
        i=0
        while i <len(ans):
            ans[i] = [beginWord]+ans[i]
            if len(ans[i])>self.min+1:
                ans.pop(i)
            else: 
                i+=1
        return ans
    def dfs(self,beginWord,endWord,wordList,ans,res):
        #print(beginWord,endWord)
        if beginWord == endWord:
            # print(res)
            self.min = min(self.min,len(res))
            ans.append(res.copy())
        for i in range(len(beginWord)):
            for j,word in enumerate(wordList):
                if (word[:i]+word[i+1:])==(beginWord[:i]+beginWord[i+1:]):
                    res.append(word)
                    if len(res)<=self.min:
                        self.dfs(word,endWord,wordList[:j]+wordList[j+1:],ans,res)
                    res.pop()
    def findLadders1(self, beginWord: str, endWord: str, wordList):
        ##BFS
        res = []
        path = []
        word = set([])
        if endWord not in wordList:
            return res
        queue_path = []
        wordSet = set(wordList)
        path.append(beginWord)
        queue_path.append(path)
        level = 1
        minlevel = len(wordList)+1
        while(len(queue_path)!=0):
            t = queue_path.pop(0)
            if len(t)>level:
                for w in word:
                    wordSet.remove(w)
                word.clear()
                level = len(t)
                if level>minlevel:
                    break
            last = t[-1]
            for i in range(len(last)):
                for ch in range(ord('a'),ord('z')+1):
                    newlast = last[:i]+chr(ch)+last[i+1:]
                    if newlast not in wordSet:
                        continue
                    # print(newlast)
                    word.add(newlast)
                    nextpath = t.copy()
                    nextpath.append(newlast)
                    print(newlast==endWord)
                    if newlast==endWord:
                        res.append(nextpath)
                        minlevel = level
                    else:
                        queue_path.append(nextpath)
        return res

                
s = Solution()
begin = "hit"
end = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

begin = "hot"
end = "dog"
wordList = ["hot","dog"]
print(s.findLadders1(begin,end,wordList))
