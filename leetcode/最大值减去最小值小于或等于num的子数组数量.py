### 程序员代码面试指南 p31
'''
给定数字arr 和整数num 共返回有多少个子数组满足如下情况：
max(arr[i..j])-min(arr[i..j])<=num
'''
###题解
## 分情况 以每个元素为首的子数组的个数
### 然后使用两个队列维持最大值 和最小值 为了找到所以满足条件的最长连续子数组

## 为了便利

class Solution:
    def findsubseq(self,arr,num):
        if arr==None or len(arr)==0 or num<0:
            return 0
        n = len(arr)
        qmin = []
        qmax = []
        i,j,res=0,0,0
        while(i<n):
            while(j<n):
                if len(qmin)==0 or j!=qmin[-1]:
                    while len(qmin)!=0 and arr[qmin[-1]]>=arr[j]:
                        qmin.pop()   
                    qmin.append(j)    
                    while len(qmax)!=0 and arr[qmax[-1]]<=arr[j]:
                        qmax.pop()
                    qmax.append(j)
                if arr[qmax[0]]-arr[qmin[0]]>num:
                    break
                j+=1
            res += j-i
            if qmin[0]==i:
                qmin.pop(0)
            if qmax[0]==i:
                qmax.pop(0)
            i+=1
        return res        

arr = [1,2,3,4,5,6]
s = Solution()
print(s.findsubseq(arr,2))