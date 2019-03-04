# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        elif len(nums)==1:
            if nums[0]==target:
                return 0
            else: 
                return -1
        if nums[0]<nums[-1] and (target<nums[0] or target>nums[-1]):
            return -1
        else: 
            index = len(nums)//2
            ans1 = self.search(nums[:index],target)
            ans2 = self.search(nums[index:],target)
            if ans1 != -1:
                return ans1
            if ans2 != -1:
                return index+ans2
            return -1

    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ### 更快的方法 相比前面的解法 减少了很多没有必要的判断（一侧无序另一半肯定有序）
        left = 0
        right = len(nums)-1
        while(left<=right):
            mid = (left + right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<nums[right]:
                if nums[mid]<target and nums[right]>=target:
                    left = mid+1
                else: 
                    right = mid-1
            else: 
                if nums[left]<=target and nums[mid]>target:
                    right = mid - 1 
                else: 
                    left = mid + 1
        return -1
s = Solution()
nums = [4,5,6,7,0,1,2]
print(s.search1(nums,0))