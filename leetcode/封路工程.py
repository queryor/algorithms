import sys
import heapq

# 最小生成树，动态规划解法
class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()
 
    def get_nodenum(self):
        return len(self.maps)
 
    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count
 
 
    def prim(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum-1:
            return res
        res = []
        seleted_node = [0]
        candidate_node = [i for i in range(1, self.nodenum)]
        
        while len(candidate_node) > 0:
            begin, end, minweight = 0, 0, 9999
            for i in seleted_node:
                for j in candidate_node:
                    if self.maps[i][j] < minweight:
                        minweight = self.maps[i][j]
                        begin = i
                        end = j
            res.append([begin, end, minweight])
            seleted_node.append(end)
            candidate_node.remove(end)
        return res

if __name__ == "__main__":
    # 读取第一行的n
    n,m = [int(i) for i in sys.stdin.readline().strip().split()]
    flag = sys.stdin.readline().strip()
    E = {}
    ans = []
    edge = [[9999 for i in range(n)]for i in range(n)]
    for i in range(n):
        edge[i][i]=0
    for i in range(m):
        a,b = [int(i) for i in sys.stdin.readline().strip().split()]
        E["{}_{}".format(a-1,b-1)]=i+1
        E["{}_{}".format(b-1,a-1)]=i+1
        if flag[a-1]!=flag[b-1]:##删选掉不合规的
            edge[a-1][b-1]=1
            edge[b-1][a-1]=1
    
    
    graph = Graph(edge)

    result = graph.prim()
    ans = []
    for i in range(len(result)):
        a,b,w = result[i]
        ans.append(E["{}_{}".format(a,b)])
    print(len(ans))
    print(" ".join([str(i) for i in ans]))
