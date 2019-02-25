# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        l = None
        for s in strs:
            if l==None:
                l = len(s)
            elif len(s)<l:
                l = len(s)
        res = ''
        print(l)
        if l == 0:
            return res
        for i in range(l):
            c = strs[0][i]
            for s in strs:
                if s[i]!=c:
                    return res
            res+=c
        return res
        



i = ["","b"]
s = Solution()
print(s.longestCommonPrefix(i))
