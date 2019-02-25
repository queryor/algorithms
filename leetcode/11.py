#  Container With Most Water
#  Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution:
    def maxArea1(self, height):
        # Time Limit Exceeded
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
               area = min(height[i],height[j])*(j-i)
               if area > res:
                   res = area 
        return res
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            h1, h2 = height[i], height[j]
            area = (j - i) * min(h1, h2)
            max_area = max(max_area, area)
            
            if h1 < h2:
                i += 1
            else:
                j -= 1
                
        return max_area
n = [1,8,6,2,5,4,8,3,7]
s = Solution()
print(s.maxArea(n))