# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

# 和78题差不多 就是多一个重复元素的处理

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans=[]
        def subsetsDFS(nums,k,res=[]):
            if k==0:
                if res not in ans:
                    ans.append(res)
            else:
                for i,n in enumerate(nums):
                    if k > (len(nums)-i): ##后面的数字个数不够了就不必要再递归了
                        break
                    ### 防止出现重复
                    if i!=0 and n==nums[i-1]:
                        continue
                    res.append(n)
                    t = res.copy()
                    subsetsDFS(nums[i+1:],k-1,t)
                    res.pop()
        res = []
        for k in range(len(nums)+1):
            subsetsDFS(nums,k,res)
        return ans
