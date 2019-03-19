# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:

# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
class Solution:
    def singleNumber(self, nums):
        # 利用hash map
        s = {}
        if len(nums)<2:
            return -1
        if len(nums)==2:
            return nums
        for n in nums:
            if n not in s:
                s[n]=1
            else:
                s.pop(n)
        ans = []
        for key in s.keys():
            ans.append(key)
        return ans
s = Solution()
i = [1,2,1,3,2,5]
print(s.singleNumber(i))
