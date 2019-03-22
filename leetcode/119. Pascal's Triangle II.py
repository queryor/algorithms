class Solution:
    def getRow(self, rowIndex: int):
        res = [1]
        if rowIndex == 0:
            return res
        for i in range(2,rowIndex+2):
            ans = [1 for j in range(i)]
            for j in range(1,i-1):
                ans[j]=res[j]+res[j-1]
            res = ans
        return res
        