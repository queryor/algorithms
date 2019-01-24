# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                #print(s[i:j+1])
                if self.isright(s[i:j+1]) and j-i+1>max:
                    max = j+1-i
                    #print(max,s[i:j+1])
        return max
    def isright(self,s):
        dict = {}
        for i in s:
            if i not in dict:
                dict[i]=0
            else:
                return False
        return True
    
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {}
        start = 0
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c not in dictionary or dictionary[c]<start:
                size  = i - start + 1
                if size > ans:
                    ans = size 
            else:
                start = dictionary[c]+1
            dictionary[c] = i
        return ans
    
n = "abcdabc"
s = Solution()
print(s.lengthOfLongestSubstring1(n))