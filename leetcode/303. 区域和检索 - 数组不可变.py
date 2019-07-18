'''
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
#线段树
class SegTreeNode:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.val = 0
        self.lazy = 0
class SegTree:
    def __init__(self,n):
        #print(n)
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
            self.array[root].val = self.array[root*2+1].val+self.array[root*2+2].val
            self.array[root].l = istart
            self.array[root].r = iend
    '''
    功能：线段树的区间查询
    root：当前线段树的根节点下标
    [nstart, nend]: 当前节点所表示的区间
    [qstart, qend]: 此次查询的区间
    '''
    def query(self,root,nstart,nend,qstart,qend):
        ### 查询范围超出
        if qstart>nend or qend<nstart:
            return 0
        elif qstart<=nstart and qend>=nend:
            return self.array[root].val
        #self.pushDown(root)
        mid = (nstart+nend)//2
        return self.query(root*2+1,nstart,mid,qstart,qend)+self.query(root*2+2,mid+1,nend,qstart,qend)

class NumArray:

    def __init__(self, nums):
        self.n = len(nums)
        if self.n>0:
            self.stree = SegTree(len(nums))
            self.stree.build(0,nums,0,len(nums)-1)
    def sumRange(self, i: int, j: int) -> int:
        if self.n>0:
            return self.stree.query(0,0,self.n-1,i,j)
        else:
            return None

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)