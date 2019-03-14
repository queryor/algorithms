# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example:

# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

## 遍历每一行 就当成了 84 题
## 参考 https://www.hrwhisper.me/leetcode-largest-rectangle-in-histogram-and-leercode-maximal-rectangle/ 以及image/85.jpg


class Solution:
    def maximalRectangle(self, matrix) -> int:
        if matrix == None or len(matrix)==0 or len(matrix[0])==0:
            return 0
        m,n = len(matrix),len(matrix[0])
        pre = [0 for i in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="0":
                    pre[j]=0
                else:
                    pre[j]=pre[j]+1
            res = max(res,self.largestRectangleArea(pre))
        return res

    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights.append(0)
        res = 0
        i=0
        while i < (len(heights)):
            if len(stack)==0 or heights[i]>heights[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                cur = stack[-1]
                stack.pop()
                res = max(res,heights[cur]*(i if len(stack)==0 else (i-stack[-1]-1)))
        return res