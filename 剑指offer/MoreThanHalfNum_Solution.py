# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = {}
        for n in numbers:
            n = str(n)
            if count.has_key(n):
                count[n]+=1
            else:
                count[n]=1
        flag = 0
        for k,v in count.items():
            if v>len(numbers)/2:
                return(int(k))
        return 0

s = [1,2,3]
a = Solution()
print a.MoreThanHalfNum_Solution(s)