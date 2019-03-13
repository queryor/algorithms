# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 
class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights.append(0)
        res = 0
        for i in range(len(heights)):
            if len(stack)==0 or heights[i]>heights[stack[-1]]:
                stack.append(i)
            else:
                cur = stack[-1]
                stack.pop()
                
