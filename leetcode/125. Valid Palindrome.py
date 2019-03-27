# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ##直接遍历判断
        ## 首先去除非字母 
        # 大写转换成小写
        s = s.lower()
        i = 0
        while i<len(s):
            if (ord(s[i])>=ord('a') and ord(s[i])<=ord('z'))or (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')) :
                i+=1
            else: 
                s = s[:i]+s[i+1:]
        # print(s)
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True

    def isPalindrome1(self,s:str):
        if len(s) == 0:
            return True
        
        lo, hi = 0, len(s) - 1
        
        while lo<hi:
            if not s[lo].isalnum():
                lo += 1; continue
            if not s[hi].isalnum():
                hi -= 1; continue
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1; hi -= 1
        
        return True