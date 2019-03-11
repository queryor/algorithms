# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 先从后往前找第一个单词前的空格，然后直接通过索引得到长度
        # 需要注意去除末尾的空格
        l = len(s)
        if l==0:
            return 0
        i = l-1
        while i >=0:
            if s[i]==' ':
                if i==l-1:
                    i-=1
                    l-=1
                    continue
                else:
                    return l-i-1
            i-=1
        return l
                

s = Solution()
i = " World       "
print(s.lengthOfLastWord(i))