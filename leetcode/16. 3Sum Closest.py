# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        res = None
        diff = None
        nums.sort()
        length=len(nums)
        for i in range(length-2): #[8]
            #if nums[i]>0: break #[7]
            #if i>0 and nums[i]==nums[i-1]: continue #[1]
            l, r = i+1, length-1 #[2]
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if res==None and diff==None:
                    res = total
                    diff = abs(total-target)
                if abs(total-target)<diff:
                    res = total
                    diff = abs(total-target)
                if total<target: #[3]
                    l+=1
                elif total>target: #[4]
                    r-=1
                else: #[5]
                    return target
        return res
        



s  = Solution()
a =[-1, 2, 1, -4]
target = 1
print(s.threeSumClosest(a,target))