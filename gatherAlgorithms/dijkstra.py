
max_float=float('inf')
## dijkstra算法实现
def Dijkstra(points,graph,start,end):
    map = [[ max_float for i in range(points)] for j in range(points)]
    pre = [0]*(points) #记录前驱
    vis = [0]*(points) #记录节点遍历状态
    dis = [max_float for i in range(points)] #保存最短距离
    road = [0]*(points) #保存最短路径
    roads = []
    map = graph
 
    for i in range(points):#初始化起点到其他点的距离
        if i == start :
            dis[i] = 0
        else :
            dis[i] = map[start][i]
        if map[start][i] != max_float:
            pre[i] = start
        else :
            pre[i] = -1
    vis[start] = 1
    for i in range(points):#每循环一次确定一条最短路
        min = max_float
        for j in range(points):#寻找当前最短路
            if vis[j] == 0 and dis[j] < min :
                t = j
                min = dis[j]
        vis[t] = 1 #找到最短的一条路径 ,标记
        for j in range(points):
            if vis[j] == 0 and dis[j] > dis[t]+ map[t][j]:
                dis[j] = dis[t] + map[t][j]
                pre[j] = t
        if t == end:
            break
    p = end
    len = 0
    while p >= 0 and len < points:
        road[len] = p
        p = pre[p]
        len += 1
    mark = 0
    len -= 1
    while len >= 0:
        roads.append(road[len])
        len -= 1
    return dis[end],roads
 
#固定map图
def map():
    map = [[max_float, max_float, max_float, max_float, max_float, max_float],
           [max_float, max_float, 2, 3, max_float, 7],
           [max_float, 2, max_float, max_float, 2, max_float],
           [max_float, 3, max_float, max_float, max_float, 5],
           [max_float, max_float, 2, max_float, max_float, 3],
           [max_float, 7, max_float, 5, 3, max_float]
           ]
    i= input("输入起点和终点：")
    s,e=i.split(" ")
    dis,road = Dijkstra(6,map,int(s),int(e))
    print("最短距离：",dis)
    print("最短路径：",road)
 
#输入边关系构造map图
def createmap():
    a,b = input("输入节点数和边数：").split()
    n = int(a)
    m = int(b)
    map = [[ max_float for i in range(n+1)] for j in range(n+1)]
    for i in range(m+1):
        x,y,z = input("输入两边和长度：").split()
        point = int(x)
        edge = int(y)
        map[point][edge] = float(z)
        map[edge][point] = float(z)
    s,e = input("输入起点和终点：").split()
    start = int(s)
    end = int(e)
    dis,road = Dijkstra(n,m,map,start,end)
    print("最短距离：",dis)
    print("最短路径：",road)
 
if __name__=='__main__':
    map()
