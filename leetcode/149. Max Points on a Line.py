'''Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
import math
## 计算几何题
class Solution:
    def maxPoints(self, points) -> int: 
        ## 利用斜率的方法 因为要用到除法 精度无法保证  当 [[0,0],[94911151,94911150],[94911152,94911151]]  点1和点2 到 点0 的斜率都是一样的 但是其实不在同一直线是哪个
        n = len(points)
        ans = 1
        dic = {}
        for i in range(n):
            same, p = 1, 0
            for j in range(i + 1, n):
                if points[i]== points[j]:
                    same += 1
                    continue
                elif points[i][0] != points[j][0]:
                    p = (points[j][1] - points[i][1]) * 1.0 / (points[j][0] - points[i][0])
                else:
                    p = float('inf')
                if p in dic:
                    dic[p] += 1
                else:
                    dic[p] = 1
            ans = max(ans, same)
            for j in dic:
                ans = max(ans, dic[j] + same)
            dic = {}
        return ans
# 由于通过斜率来判断共线需要用到除法，而用 double 表示的双精度小数在有的系统里不一定准确，为了更加精确无误的计算共线，我们应当避免除法，从而避免无线不循环小数的出现，那么怎么办呢，
# 我们把除数和被除数都保存下来，不做除法，但是我们要让这两数分别除以它们的最大公约数，
# 这样例如8和4，4和2，2和1，这三组商相同的数就都会存到一个映射里面，同样也能实现我们的目标，而求 GCD 的函数如果用递归来写那么一行就搞定了，
# 算是牺牲了空间来保证精度吧
    def gcd(self,a, b):
        return a if b==0 else self.gcd(b,a%b)
    def maxPoints1(self,points)->int:
        n = len(points)
        if n == 0 :
            return 0
        ans = 1
        dic = {}
        for i in range(n):
            same, p = 1, 0
            for j in range(i + 1, n):
                if points[i]== points[j]:
                    same += 1
                    continue
                dx = points[j][0]-points[i][0]
                dy = points[j][1]-points[i][1]
                d = self.gcd(dx, dy)
                p = "{}_{}".format(int(dx/d),int(dy/d))
                if p in dic:
                    dic[p] += 1
                else:
                    dic[p] = 1
            #print(dic)
            ans = max(ans, same)
            for j in dic:
                ans = max(ans, dic[j] + same)
            dic = {}
        return ans
i = [[2,3],[3,3],[-5,3]]
s = Solution()
print(s.maxPoints1(i))