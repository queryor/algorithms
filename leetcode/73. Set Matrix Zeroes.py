# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 巧妙方法
        obj = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = obj
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = obj
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] is obj:
                    matrix[i][j] = 0
    def setZeroes1(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #利用第一行第一列来存flag

        ## 先要判断第一行第一列有没有0
        row_zero=False
        col_zero=False
        r_num = len(matrix)
        c_num = len(matrix[0])
        if r_num==0 or c_num == 0:
            return -1
        # 检测第一行
        for i in range(c_num):
            if matrix[0][i]==0:
                row_zero=True
        # 检测第一列
        for i in range(r_num):
            if matrix[i][0]==0:
                col_zero=True
        # 遍历数组 设置flag
        for i in range(1,r_num):
            for j in range(1,c_num):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        # 遍历数组 根据 flag 修改值
        for i in range(1,r_num):
            for j in range(1,c_num):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        # 修改第一行 和 第一列
        if row_zero:
            for i in range(c_num):
                matrix[0][i]=0
        if col_zero:
            for i in range(r_num):
                matrix[i][0]=0