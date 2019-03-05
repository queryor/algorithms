# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

class Solution:
    def combinationSum(self, candidates, target: int):
#     Runtime: 68 ms, faster than 83.26% of Python3 online submissions for Combination Sum.
#     Memory Usage: 12.9 MB, less than 5.14% of Python3 online submissions for Combination Sum.
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
                        self.combinationSumDFS(candidates[i:],target-v,ans,res)
                        res.pop()

            


        

s =Solution()
i = [2,3,6,7]
target = 7
print(s.combinationSum(i,target))