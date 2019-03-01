# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# Example 1:

# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        Dict = dict.fromkeys(words,0)
        for word in words:
            Dict[word]+=1
        if len(s)==0 or len(words)==0:
            return ans
        totword = len(words)
        wordlen = len(words[0])
        slen = len(s)-totword*wordlen
        for i in range(0,slen+1):
            cnt = dict.fromkeys(words,0)
            okNum = 0
            for k in range(0,totword):
                cur = s[i+k*wordlen:i+(k+1)*wordlen]
                if cur in Dict:
                    cnt[cur]+=1
                    if(cnt[cur]>Dict[cur]):
                        break
                    okNum = okNum +1
            if okNum == totword:
                ans.append(i)
        
        return ans
    def findSubstring1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        word_len = len(words[0])
        word_total = (len(words) - 1) * word_len
        ans = []
        word_cnt = collections.Counter(words)
        for i in range(word_len):
            start = i
            cur_cnt = collections.Counter()
            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j: j + word_len]
                if word in word_cnt:
                    cur_cnt[word] += 1
                    while cur_cnt[word] > word_cnt[word]:
                        cur_cnt[s[start: start + word_len]] -= 1
                        start += word_len
                else:
                    cur_cnt.clear()
                    start = j + word_len
                
                if(start + word_total == j):
                    ans.append(start)
        return ans




