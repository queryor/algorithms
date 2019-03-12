# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        ### 二分查找 加上 坐标变换
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        if m==0 or n==0:
            return False
        if target<matrix[0][0] or target>matrix[m-1][n-1]:
            return False
        left=0
        right = m*n-1
        while left<=right:
            mid = (left+right)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]<target:
                left=mid+1
            else: 
                right=mid-1
        return False