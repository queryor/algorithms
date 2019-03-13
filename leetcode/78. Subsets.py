# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    def subsets(self, nums):
        ans=[]
        def subsetsDFS(nums,k,res=[]):
            if k==0:
                ans.append(res)
            else:
                for i,n in enumerate(nums):
                    if k > (len(nums)-i): ##后面的数字个数不够了就不必要再递归了
                        break
                    res.append(n)
                    t = res.copy()
                    subsetsDFS(nums[i+1:],k-1,t)
                    res.pop()
        res = []
        for k in range(len(nums)+1):
            subsetsDFS(nums,k,res)
        return ans