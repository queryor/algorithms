# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution:
    def combinationSum2(self, candidates, target: int):
        ans = []
        res = []
        candidates.sort()
        self.combinationSumDFS(candidates,target,ans,res)
        return ans
    def combinationSumDFS(self,candidates,target,ans,res=[]):
        if len(candidates)==0:
            res = []
        else:
            for i,v in enumerate(candidates):
                if i!=0 and v == candidates[i-1]: # 防止出现两个数字一样的情况 
                    continue
                if v == target:
                    res.append(v)
                    t = res.copy()
                    ans.append(t)
                    res.pop()
                else:
                    if target - v < 0 :
                        break
                    else:
                        res.append(v)
                        self.combinationSumDFS(candidates[i+1:],target-v,ans,res)
                        res.pop()
s =Solution()
i = [10,1,2,7,6,1,5]
target = 8
print(s.combinationSum2(i,target))