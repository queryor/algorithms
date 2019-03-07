# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    def permute(self, nums):
        out = []
        temp = []
        def helper(nums, temp, out):
            
            if not nums:
                out.append(temp)
                return

            for i in range(len(nums)):
                new_temp = temp + [nums[i]]
                new_nums = nums[:i] + nums[i+1:]
                helper(new_nums, new_temp, out)
               
        helper(nums, temp, out)
        return out

s = Solution()
i = [1,2,3]
print(s.permute(i))