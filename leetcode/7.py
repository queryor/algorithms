# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
    
        sign = 1 if x >=0 else -1
        n = sign*int(str(abs(x))[::-1])
        if n <= -1*(2**31) or n > 2**31:
            return 0 
        return n

x = -10
s = Solution()
print(s.reverse(x))