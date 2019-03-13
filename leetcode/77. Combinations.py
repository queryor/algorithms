# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    def combine(self, n: int, k: int):
        ## 递归
        if n==0 or k==0:
            return []
        ans = []
        def combineDFS(nums,k,res=[]):
            if k==0:
                ans.append(res)
            else:
                for i,n in enumerate(nums):
                    if k > (len(nums)-i): ##后面的数字个数不够了就不必要再递归了
                        break
                    res.append(n)
                    t = res.copy()
                    combineDFS(nums[i+1:],k-1,t)
                    res.pop()
        nums = [i+1 for i in range(n)]
        res = []
        combineDFS(nums,k,res)
        return ans

s = Solution()
print(s.combine(4,2))
        