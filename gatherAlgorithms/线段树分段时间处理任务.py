#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
'''
提供区间的更新和区间的查询
'''
import sys
import math
class seqnode:
    def __init__(self):
        self.val = set()
        self.lazy_a = set()
        self.lazy_d = set()
class seqTree:
    def __init__(self,n):
        self.arr = [seqnode() for i in range(2**(math.ceil(math.log2(n))+1))]
    def pushdown(self,root):
        if len(self.arr[root].lazy_a)!=0:
            self.arr[root * 2 + 1].lazy_a=self.arr[root*2+1].lazy_a.union(self.arr[root].lazy_a)
            self.arr[root * 2 + 2].lazy_a=self.arr[root*2+2].lazy_a.union(self.arr[root].lazy_a)
            self.arr[root * 2 + 1].val = self.arr[root*2+1].val.union(self.arr[root].lazy_a)
            self.arr[root * 2 + 2].val = self.arr[root*2+2].val.union(self.arr[root].lazy_a)
            self.arr[root].lazy_a = set()
        if len(self.arr[root].lazy_d)!=0:
            #print(root,self.arr[root*2+1].val,self.arr[root*2+2].val,self.arr[root].lazy_d)
            self.arr[root * 2 + 1].lazy_d =self.arr[root*2+1].lazy_d.union(self.arr[root].lazy_d)
            self.arr[root * 2 + 2].lazy_d = self.arr[root*2+2].lazy_d.union(self.arr[root].lazy_d)
            self.arr[root*2+1].val-=self.arr[root].lazy_d
            self.arr[root*2+2].val-=self.arr[root].lazy_d
            #print(self.arr[root * 2 + 1].val, self.arr[root * 2 + 2].val)
            self.arr[root].lazy_d=set()
    def query(self,root,nstart,nend,qstart,qend):
        if qstart>nend or qend<nstart:
            return set()
        elif qstart<=nstart and qend >=nend:
            return self.arr[root].val
        self.pushdown(root)
        mid = (nstart+nend)//2
        return  self.query(root*2+1,nstart,mid,qstart,qend).union(self.query(root*2+2,mid+1,nend,qstart,qend))
    def update(self,root,nstart,nend,l,r,v,opt):
        #print(root,nstart,nend,l,r)
        if l>nend or r<nstart:
            return
        if l<=nstart and r>=nend:
            if opt == 1:
                self.arr[root].lazy_a.add(v)
                self.arr[root].val.add(v)
                return
            else:
                self.arr[root].lazy_d.add(v)
                #print(root,self.arr[root].val,self.arr[1].lazy_a)
                self.arr[root].val.remove(v)
                #print(self.arr[root].val)
                return
        self.pushdown(root)
        mid = (nstart+nend)//2
        self.update(root*2+1,nstart,mid,l,r,v,opt)
        self.update(root*2+2,mid+1,nend,l,r,v,opt)
        self.arr[root].val = self.arr[root*2+1].val.union(self.arr[root*2+2].val)
if __name__ == "__main__":
    n,m,t = [int(i) for i in sys.stdin.readline().strip().split()]
    tree = seqTree(n)
    for i in range(m):
        line = [int(i) for i in sys.stdin.readline().strip().split()]
        opt = line[0]
        if opt == 1 or opt==2:
            tree.update(0,0,n-1,line[1]-1,line[2]-1,line[3],opt)
            #print(tree.arr[4].val)
        else:
            s = tree.query(0,0,n-1,line[1]-1,line[2]-1)
            print(len(s))