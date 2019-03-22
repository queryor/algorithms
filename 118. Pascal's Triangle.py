# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        res = []
        ans = [1]
        res.append(ans)
        if numRows == 1:
            return res
        for i in range(2,numRows+1):
            ans = [1 for j in range(i)]
            for j in range(1,i-1):
                ans[j]=res[-1][j]+res[-1][j-1]
            res.append(ans)
        return res