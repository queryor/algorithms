# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2

# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
# assume that your function returns 2^31 − 1 when the division result overflows.
INT_MAX = pow(2,31)-1
INT_MIN = -pow(2,31)
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0 or (dividend==INT_MIN and divisor==-1):
            return INT_MAX
        m = abs(dividend)
        n = abs(divisor)
        res = 0
        sign = (dividend<0) is (divisor<0)
        while m>=n:
            temp,i = n,1
            while m>=(temp<<1):
                temp<<=1
                i<<=1
            res+=i
            m-=temp
        if not sign:
            res = -res               
        return min(max(INT_MIN,res),INT_MAX)

dividend = 7
divisor = -3
s = Solution()
print(s.divide(dividend,divisor))