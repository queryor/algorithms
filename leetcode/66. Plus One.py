# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution:
    def plusOne(self, digits):
    # 当成一个十进制数进行加一操作
    # 需要注意9的进位操作以及全是9的加一位操作    
    # Runtime: 40 ms, faster than 59.18% of Python3 online submissions for Plus One.
    # Memory Usage: 13.1 MB, less than 5.29% of Python3 online submissions for Plus One.
        right = len(digits)-1
        while right>=0:
            if digits[right]<9:
                digits[right]+=1
                break
            else: 
                digits[right]=0
                if right == 0:
                    digits.insert(0,1)
                    break
                right-=1
        return digits

s = Solution()
i = [9,9,9,9]
print(s.plusOne(i))