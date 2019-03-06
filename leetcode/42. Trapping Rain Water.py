# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap1(self, height) -> int:
        #去掉两边0然后提高一定格数水平线，递归求解。 ！！！超时
        return self.trapDFS(height)
    def trapDFS(self,height,ans=0):
        while(len(height)>=0):
            if len(height)<=1:
                return ans
            for left in range(len(height)):
                if height[left]>0:
                    break
            for right in range(len(height)-1,-1,-1):
                if height[right]>0:
                    break
            min_y = height[left]
            for i in range(left,right+1):
                if height[i]>0 and height[i]<min_y:
                    min_y = height[i]
            for i in range(left,right+1):
                if height[i]==0:
                    ans+=min_y
                else:
                    height[i]-=min_y
            height = height[left:right+1]
    def trap(self, height) -> int:
        # 左右两个指针。left和right两个指针分别指向数组的首尾位置，从两边向中间扫描，在当前两指针确定的范围内，先比较两头找出较小值，如果较小值是left指向的值，则从左向右扫描，
        # 如果较小值是right指向的值，则从右向左扫描，若遇到的值比当较小值小，则将差值存入结果，如遇到的值大，则重新确定新的窗口范围，以此类推直至left和right指针重合，
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            mn = min(height[left],height[right])
            if mn == height[left]:
                left+=1
                while(left<right and height[left]<mn):
                    res+=mn-height[left]
                    left+=1
            else: 
                right-=1
                while(left<right and height[right]<mn):
                    res+=mn-height[right]
                    right-=1
        return res
    def trap2(self,height)->int:
        # 实用stack的方法博主感觉更容易理解，我们的做法是，遍历高度，如果此时栈为空，
        # 或者当前高度小于等于栈顶高度，则把当前高度的坐标压入栈，注意我们不直接把高度压入栈，而是把坐标压入栈，
        # 这样方便我们在后来算水平距离。当我们遇到比栈顶高度大的时候，就说明有可能会有坑存在，可以装雨水。
        # 此时我们栈里至少有一个高度，如果只有一个的话，那么不能形成坑，我们直接跳过，如果多余一个的话，那么此时把栈顶元素取出来当作坑，新的栈顶元素就是左边界，
        # 当前高度是右边界，只要取二者较小的，减去坑的高度，长度就是右边界坐标减去左边界坐标再减1，二者相乘就是盛水量啦
        # 上面的方法速度更快
        stack = []
        i = 0
        res = 0
        n = len(height)
        while i<n:
            if len(stack)==0 or height[i]<=height[stack[-1]]:
                stack.append(i)
                i+=1
            else: 
                t = stack.pop()
                if len(stack)==0:
                    continue
                res+=(min(height[i],height[stack[-1]])-height[t])*(i-stack[-1]-1)
        return res        

                
s = Solution()
i = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap2(i))