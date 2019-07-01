'''
https://leetcode-cn.com/contest/biweekly-contest-3/problems/path-with-maximum-minimum-value/
给你一个 R 行 C 列的整数矩阵 A。矩阵上的路径从 [0,0] 开始，在 [R-1,C-1] 结束。

路径沿四个基本方向（上、下、左、右）展开，从一个已访问单元格移动到任一相邻的未访问单元格。

路径的得分是该路径上的 最小 值。例如，路径 8 →  4 →  5 →  9 的值为 4 。

找出所有路径中得分 最高 的那条路径，返回其 得分。

 

示例 1：



输入：[[5,4,5],[1,2,6],[7,4,6]]
输出：4
解释： 
得分最高的路径用黄色突出显示。 
示例 2：



输入：[[2,2,1,2,2,2],[1,2,2,2,1,2]]
输出：2
示例 3：



输入：[[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
输出：3
 

提示：

1 <= R, C <= 100
0 <= A[i][j] <= 10^9
'''
from heapq import *
class Solution:
    def maximumMinimumPath(self, A) -> int:
        ## 直接DFS 超时
        R = len(A)
        C = len(A[0])
        flag = [[0 for i in range(C)]for i in range(R)]
        res = [0]
        ans = A[0][0]
        flag[0][0]=1
        self.dfs(A,flag,0,0,R,C,ans,res)
        print(flag)
        return max(res)
    def dfs(self,A,flag,i,j,R,C,ans,res):
        if i-1>=0 and flag[i-1][j]==0:
            self.fun(A,flag,i-1,j,R,C,ans,res)
        if j+1<C and flag[i][j+1]==0:
            self.fun(A,flag,i,j+1,R,C,ans,res)
        if i+1<R and flag[i+1][j]==0:
            self.fun(A,flag,i+1,j,R,C,ans,res)
        if j-1>=0 and flag[i][j-1]==0:
            self.fun(A,flag,i,j-1,R,C,ans,res)
    

    def fun(self,A,flag,i,j,R,C,ans,res):
        if res!=[] and A[i][j]<=max(res):
            flag[i][j]=1
            return
        ans = min(ans,A[i][j])
        print(i,j,ans,res)
        if i==R-1 and j==C-1:
            if ans!=0:
                res.append(ans)
            return
        flag[i][j]=1
        self.dfs(A,flag,i,j,R,C,ans,res)
        flag[i][j]=0
    def maximumMinimumPath1(self, A) -> int:
        #贪心 使用优先队列
        if not A or not A[0]:
            return 0
        
        m, n = len(A), len(A[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        queue = [[-A[0][0], 0, 0]] #Python默认最小堆，因此需要手动用相反数实现最大堆……
        visited = set([0,0])
        heapify(queue)

        while queue:
            score, x0, y0 = heappop(queue) #把目前队里最优的点找出来，三个值分别代表分数， X坐标， Y坐标
            if [x0, y0] == [m - 1, n - 1]: #如果已经到终点了
                return -score #输出结果时记得再取一次相反数
            
            for k in range(4): #找四个可能的邻居点
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:#邻居点可走
                    visited.add((x, y))
                    heappush(queue, [max(score, -A[x][y]), x, y]) #邻居点入队，调整分数，因为取了相反数所以找最小值用max不用min
        
s = Solution()
i = [[5,3,2,4,2,5],[1,2,2,5,0,1],[0,5,5,4,1,0],[5,4,0,2,5,3],[3,1,1,1,5,1],[3,3,4,3,2,5],[2,0,2,3,2,3]]
print(s.maximumMinimumPath1(i))    