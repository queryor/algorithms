#参考链接 https://blog.csdn.net/niushuai666/article/details/6662911

'''
简单理解题意就是有很多点 给你一定量的连接 最后问有多少个独立的连通图。
解题思路就是并查集 参考上面的链接，很有趣可以加深理解。

用pre[]数组记录每个节点的上一级，如果两个节点拥有最终的上级，那么说明是同一个连通图的。
如果需要连接的两个点不在同一个连通图中，便通过使他们最终上级一样的方式连通他们。
同时可以通过路径压缩算法优化。
'''


class Solution:
    def union(self,n,s):
        '''
        n：节点总个数
        s: 所有的连接
        return：返回有多少个独立连通子图
        '''
        ## 默认自己的上级就是自己
        self.pre = [i for i in range(n)]
        group = n
        for link in s:
            x,y = link
            root1 = self.unionsearch(x)
            root2 = self.unionsearch(y)
            if root1!=root2:
                self.pre[root1] = root2
                group-=1
        return group    

    def unionsearch(self,root):
        '''
        找到最终上级
        '''
        son = root
        while root != self.pre[root]:
            root = self.pre[root]
        ## 路径压缩
        while son !=root:
            tmp = self.pre[son]
            self.pre[son]=root
            son = tmp
        return root

s = Solution()
## 模拟的8个点的数据
i = [[0,2],[1,2],[0,1],[4,5],[3,6],[3,7]]
print(s.union(8,i))