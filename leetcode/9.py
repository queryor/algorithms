# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        if len(s)==0:
            return True
        else:
            for i in range(len(s)//2):
                if s[i]!=s[-i-1]:
                    return False
        return True