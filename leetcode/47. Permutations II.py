# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    def permuteUnique(self, nums):
        out = []
        temp = []
        def helper(nums, temp, out):
            
            if not nums:
                out.append(temp)
                return

            for i in range(len(nums)):
                if(i!=0 and nums[i]==nums[i-1]):
                    continue
                new_temp = temp + [nums[i]]
                new_nums = nums[:i] + nums[i+1:]
                helper(new_nums, new_temp, out)
               
        helper(nums, temp, out)
        return out

s = Solution()
i = [1,1,2]
print(s.permuteUnique(i))