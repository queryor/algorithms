# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### 相当于暴力法 insert
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        else:     
            for i in range(n):
                for j in range(m+i+1):
                    if nums1[j]>=nums2[i]:
                        break                    
                nums1.insert(j,nums2[i])
            #nums1 = nums1[:m+n]
            for i in range(n):
                nums1.pop()
        #print(nums1)
    
    def merge1(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### 从末尾 依次取大的
        i,j= m-1,n-1
        for idx in range(m+n-1,-1,-1):
            if j==-1 or i>=0 and nums1[i]>nums2[j]:
                nums1[idx]=nums1[i]
                i-=1
            else: 
                nums1[idx]=nums2[j]
                j-=1
        #print(nums1)
s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(s.merge1(nums1,3,nums2,3))