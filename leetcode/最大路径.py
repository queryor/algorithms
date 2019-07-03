import sys

def dfs(Edge,Node,res,ans,node_n,pre):
    if len(Node[node_n])==1 and Node[node_n][0]==pre:
        ans[0] = max(ans[0],res)
        return
    else:
        for i in Node[node_n]:
            if i !=pre:
                w = Edge["{}_{}".format(min(node_n,i),max(node_n,i))]
                res+=w 
                dfs(Edge,Node,res,ans,i,node_n)
                res-=w

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    Edge = {}
    Node = {}
    for i in range(n-1):
        s,e,w = [int(i) for i in sys.stdin.readline().strip().split()]
        if s not in Node:
            Node[s]=[e]
        else:
            Node[s].append(e)
        if e not in Node:
            Node[e]=[s]
        else:
            Node[e].append(s)
        Edge["{}_{}".format(min(s,e),max(s,e))]=w
    m = int(sys.stdin.readline().strip())
    for i in range(m):
        node_n = int(sys.stdin.readline().strip())
        ans = [0] 
        res = 0
        dfs(Edge,Node,res,ans,node_n,pre=-1)
        print(ans[0])
