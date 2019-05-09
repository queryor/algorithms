# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        wordset  = set(wordList)
        if endWord not in wordset:
            return 0
        quene = [beginWord]
        res = 0
        while(len(quene)!=0):
            for k in range(len(quene)):
                word = quene[0]
                if word == endWord:
                    return res+1
                quene = quene[1:]
                for j in range(len(word)):
                    for c in range(ord('a'),ord('z')+1):
                        newword = [i for i in word]
                        newword[j] = chr(c)
                        newword = "".join(newword.copy())
                        if str(newword) != word and newword in wordset:
                            quene.append(newword)
                            wordset.remove(newword)
            res+=1
        return 0
        


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(s.ladderLength(beginWord,endWord,wordList))