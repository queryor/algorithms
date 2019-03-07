# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# Example:

# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:

# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums) -> int:
        ## 超时
        if len(nums)<=1:
            return 0
        dp = [len(nums) for i in range(len(nums))]
        dp[0] = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if i-j <= nums[j]:
                    dp[i] = min(dp[i],dp[j]+1)
        return dp[len(nums)-1]

    def jump1(self, nums) -> int:
        ## 还是超时
        if len(nums)<=1:
            return 0
        dp = [[0,len(nums)] for i in range(len(nums))]
        dp[0][1] = 0
        for i in range(1,len(nums)):
            for j in range(dp[i][0],i):
                if i-j<= nums[j]:
                    if dp[i][1]>dp[j][1]+1:
                        dp[i][0]=j
                        dp[i][1]=dp[j][1]+1
        
        return dp[len(nums)-1][1]
    
    def jump2(self,nums)->int:
        ## 贪心 贪婪两次跳能跳的最远的距离
        res = 0
        n = len(nums)
        i = 0
        cur = 0
        while cur<n-1:
            res+=1
            pre = cur
            while i<=pre:
                cur = max(cur,i+nums[i])
                i+=1
            if(pre==cur):
                return -1
        return res


s = Solution()
i = [2,1]
print(s.jump2(i))