# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n)
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left]==nums[right]==target:
                return left,right
            if nums[left]<target:
                left+=1
            elif nums[left]>target:
                return -1,-1
            if nums[right]>target:
                right-=1
            elif nums[right]<target:
                return -1,-1     
        return -1,-1

    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(lgn)
        # 先二分找到最小的匹配值，然后二分找到最大的匹配值
        left_ans = 0
        right_ans = len(nums)-1
        left = 0
        right = len(nums)-1
        while left<right:
            if right==left+1:
                if nums[left]==target:
                    left_ans = left
                else: 
                    left_ans = right
                break
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else: 
                left = mid
            #print(left,right)
        left = 0
        right = len(nums)-1
        while left<right:
            if right==left+1:
                if nums[right]==target:
                    right_ans = right
                else: 
                    right_ans = left
                break
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid
            else: 
                right = mid
        if left_ans<right_ans:
            return left_ans,right_ans
        elif left_ans ==right_ans and nums[left_ans]==nums[right_ans]==target:
            return left_ans,right_ans
        else: 
            return -1,-1

s = Solution()
nums = [1]
print(s.searchRange1(nums,0))