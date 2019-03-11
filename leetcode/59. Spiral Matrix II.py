# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# Example:

# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    def generateMatrix(self, n: int):
        ans = [[0 for i in range(n)] for i in range(n)]
        row_u,col_u = n,n
        row_l,col_l = 0,0
        count = 1
        while row_u>=row_l and col_u>=col_l:
            for i in range(col_l,col_u):
                ans[row_l][i]=count
                count+=1
            for i in range(row_l+1,row_u):
                ans[i][col_u-1]=count
                count+=1
            for i in range(col_u-2,col_l-1,-1):
                ans[col_u-1][i]=count
                count+=1
            for i in range(row_u-2,row_l,-1):
                ans[i][col_l]=count
                count+=1
            row_l,col_l=row_l+1,col_l+1
            row_u,col_u=row_u-1,col_u-1

        return ans

s = Solution()
i = 10
print(s.generateMatrix(i))