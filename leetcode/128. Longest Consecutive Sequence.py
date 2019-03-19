# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums) -> int:
        ## 最简单的方法 先排序 然后依次比较 O(nlpgn)
        if len(nums)<=1:
            return len(nums)
        n = len(nums)
        nums.sort()
        max_len = 1
        count = 1
        for i in range(1,n):
            if nums[i]-nums[i-1]==0:
                continue
            if nums[i]-nums[i-1]==1:
                count+=1
                if(count>max_len):
                    max_len = count
            else:
                count=1
        return max_len
    def longestConsecutive1(self, nums) -> int:
        s = set(nums)
        res = 0 
        for val in nums:
            if val not in s:continue
            s.remove(val)
            pre = val-1
            nex = val+1
            while pre in s:
                s.remove(pre)
                pre-=1
            while nex in s:
                s.remove(nex)
                nex+=1
            res = max(res,nex-pre-1)
        return res 

s = Solution()
i = [100, 4, 200, 1, 3, 2]
i = [0,-1]
print(s.longestConsecutive1(i))