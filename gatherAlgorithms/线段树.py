## 参考https://www.cnblogs.com/TenosDoIt/p/3453089.html
### 线段树python 实现 区间最小值问题为例
import math 
import sys

class SegTreeNode:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.val = 0
        self.lazy = 0
class SegTree:
    def __init__(self,n):
        self.array = [SegTreeNode() for i in  range(2**(math.ceil(math.log2(n))+1))]
    '''
     功能：构建线段树
     root：当前线段树的根节点下标
     arr: 用来构造线段树的数组
     istart：数组的起始位置
     iend：数组的结束位置
    '''
    def build(self,root,arr,istart,iend):
        self.array[root].lazy = 0 ## 延迟标记
        if istart == iend: ## 叶子节点
            self.array[root].val = arr[istart]
            self.array[root].l = self.array[root].r = istart
        else:
            mid = (istart+iend)//2
            self.build(root*2+1,arr,istart,mid)
            self.build(root*2+2,arr,mid+1,iend)
            self.array[root].val = min(self.array[root*2+1].val,self.array[root*2+2].val)
            self.array[root].l = istart
            self.array[root].r = iend
    ### 标记域往下传递
    def pushDown(self,root):
        if self.array[root].lazy !=0:
            self.array[root*2+1].lazy += self.array[root].lazy
            self.array[root*2+2].lazy += self.array[root].lazy
            self.array[root*2+1].val += self.array[root].lazy
            self.array[root*2+2].val += self.array[root].lazy
            self.array[root].lazy = 0
    '''
    功能：线段树的区间查询
    root：当前线段树的根节点下标
    [nstart, nend]: 当前节点所表示的区间
    [qstart, qend]: 此次查询的区间
    '''
    def query(self,root,nstart,nend,qstart,qend):
        ### 查询范围超出
        if qstart>nend or qend<nstart:
            return sys.maxsize
        elif qstart<=nstart and qend>=nend:
            return self.array[root].val
        self.pushDown(root)
        mid = (nstart+nend)//2
        return min(self.query(root*2+1,nstart,mid,qstart,qend), \
            self.query(root*2+2,mid+1,nend,qstart,qend))
    '''
    功能：更新线段树中某个叶子节点的值
    root：当前线段树的根节点下标
    [nstart, nend]: 当前节点所表示的区间
    index: 待更新节点在原始数组arr中的下标
    addVal: 更新的值（原来的值加上addVal）
    '''
    def updateOne(self,root,nstart,nend,index,addVal):
        if nstart==nend:
            if index == nstart: ## 找到相应的节点
                self.array[root].val +=addVal
            return
        mid = (nstart+nend)//2
        if index <= mid:
            self.updateOne(root*2+1,nstart,mid,index,addVal)
        else:
            self.updateOne(root*2+2,mid+1,nend,index,addVal)
        self.array[root].val = min(self.array[root*2+1].val,self.array[root*2+2].val)
    '''
    功能：更新线段树中某个区间内节点的值
    root：当前线段树的根节点下标
    [nstart, nend]: 当前节点所表示的区间
    [ustart, uend]: 待更新的区间
    addVal: 更新的值（原来的值加上addVal）
    '''
    def update(self,root,nstart,nend,ustart,uend,addVal):
        ## 没有交集
        if ustart>nend or uend<nstart:
            return
        if ustart<=nstart and uend >=nend:
            self.array[root].lazy += addVal
            self.array[root].val +=addVal
            return
        self.pushDown(root)
        mid = (nstart+nend)//2
        self.update(root*2+1,nstart,mid,ustart,uend,addVal)
        self.update(root*2+2,mid+1,nend,ustart,uend,addVal)
        self.array[root].val = min(self.array[root*2+1].val,self.array[root*2+2].val)
if __name__ == "__main__":
    i = [2, 5, 1, 4, 9, 3]
    n = len(i)
    stree = SegTree(n)
    stree.build(0,i,0,n-1)
    print(stree.array[0].val,stree.array[0].l,stree.array[0].r)
    ## 查询 3 到 5 之间的最小值
    print(stree.query(0,0,5,3,5))
    ## 更新 i[5] 的值
    stree.updateOne(0,0,5,5,2)
    ## 查询 3 到 5 之间的最小值
    print(stree.query(0,0,5,3,5))
    ## 更新 区间 0 到 4 的值
    stree.update(0,0,5,0,4,2)
    ## 查询 3 到 5 之间的最小值
    print(stree.query(0,0,5,3,5))
     
