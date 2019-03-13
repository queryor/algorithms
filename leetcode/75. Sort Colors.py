# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### 最简单方法...orz 2333 速度最慢
        nums.sort()
    
    def sortColors1(self,nums) -> None:
        # count sort
        count = [0 for i in range(3)]
        for i in range(len(nums)):
            count[nums[i]]+=1
        index = 0
        for i in range(3):
            for j in range(count[i]):
                nums[index]=i
                index+=1

    def sortColors2(self,nums) -> None:
        # one pass
        left = 0
        right = len(nums)-1
        i = 0
        while i <= right: ###注意只交换到right  不然会重复交换 
            if nums[i]==0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
                i+=1
            elif nums[i]==2:
                nums[right],nums[i]=nums[i],nums[right]        
                right-=1
            else:
                i+=1            