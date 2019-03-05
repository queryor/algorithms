# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums) -> int:
        ### 利用index信息
        if len(nums)==0:
            return 1
        for i in range(len(nums)):
            while(nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]):
                nums[nums[i]-1],nums[i]= nums[i],nums[nums[i]-1]
                
                #nums[i],nums[nums[i]-1] = nums[nums[i]-1],nums[i]
        for i,num in enumerate(nums):
            if num != i+1:
                return i+1
        return len(nums)




s = Solution()
i = [3,4,-1,1]
print(s.firstMissingPositive(i))        