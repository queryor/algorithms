# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

#  http://www.cnblogs.com/grandyang/p/8887985.html 单调栈总结 
class Solution:
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