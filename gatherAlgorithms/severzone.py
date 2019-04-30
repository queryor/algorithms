## 给定图计算服务区域
import numpy as np
import matplotlib.pyplot as plt
import math


class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def dis(a:point,b:point):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def get_node(Tree,V,id,pre_p,ans=[]):
    kids = Tree[id].copy()
    if len(kids)==0:
        ans.append(id)
        return
    pro = []
    for k in kids:
        dy = V[k].y-V[id].y
        dx = V[k].x-V[id].x
        p = math.atan2(dy,dx)
        p = (p-pre_p)%(2*math.pi)
        pro.append(p)
    pro = np.array(pro)
    kids = np.array(kids)
    index = pro.argsort()
    kids = kids[index]
    for k in kids:
        p = math.atan2(V[id].y-V[k].y,V[id].x-V[k].x)
        get_node(Tree,V,k,p,ans)
    

def isRayIntersectsSegment(poi,s_poi,e_poi): #[x,y] [lng,lat]
    #输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1]==e_poi[1]: #排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if s_poi[1]>poi[1] and e_poi[1]>poi[1]: #线段在射线上边
        return False
    if s_poi[1]<poi[1] and e_poi[1]<poi[1]: #线段在射线下边
        return False
    if s_poi[1]==poi[1] and e_poi[1]>poi[1]: #交点为下端点，对应spoint
        return False
    if e_poi[1]==poi[1] and s_poi[1]>poi[1]: #交点为下端点，对应epoint
        return False
    if s_poi[0]<poi[0] and e_poi[0]<poi[0]: #线段在射线左边
        return False

    xseg=e_poi[0]-(e_poi[0]-s_poi[0])*(e_poi[1]-poi[1])/(e_poi[1]-s_poi[1]) #求交
    if xseg<poi[0]: #交点在射线起点的左侧
        return False
    return True  #排除上述情况之后

def isPoiWithinPoly(poi,poly):
    #输入：点，多边形二维数组
    #poly=[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]] 

    sinsc=0 #交点个数
    #循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
    for i in range(len(poly)-1): #[0,len-1]
        s_poi=poly[i]
        e_poi=poly[i+1]
        if isRayIntersectsSegment(poi,s_poi,e_poi):
            sinsc+=1 #有交点就加1

    return True if sinsc%2==1 else  False

if __name__ == "__main__":
    V = [point(3,3),point(5,4),point(6,5),point(5,6),point(4,1),point(5,1),point(3,4),point(4,5),point(3,5),point(2,4),point(2,1),point(1,1),point(3,2)]
    pNum = len(V)
    E = [[0 for i in range(pNum)] for i in range(pNum)]
    E = np.array(E)
    ## 边初始化
    E[0,1],E[1,0]=1,0
    E[1,2],E[2,1]=1,0
    E[1,3],E[3,1]=1,0
    E[0,4],E[4,0]=1,0
    E[4,5],E[5,4]=1,0
    E[0,6],E[6,0]=1,0
    E[6,7],E[7,6]=1,0
    E[6,8],E[8,6]=1,0
    E[0,9],E[9,0]=1,0
    E[0,10],E[10,0]=1,0
    E[10,11],E[11,10]=1,0
    E[10,12],E[12,10]=1,0
    fig = plt.figure() 
    axes = fig.add_subplot(1,1,1)
    x = [i.x for i in V]
    y = [i.y for i in V]
    axes.scatter(x,y,color='r')
    for i in range(pNum):
        for j in range(pNum):
            if E[i,j]==1:
                axes.plot([V[i].x,V[j].x],[V[i].y,V[j].y],color='b')
    #构建树结构
    Tree = []
    for i in range(pNum):
        tree_t = []
        for j in range(pNum):
            if E[i,j]==1:
                tree_t.append(j)
        Tree.append(tree_t)
    print(Tree)
    ans = []
    get_node(Tree,V,0,0.0,ans)
    ans.append(ans[0])
    print(ans)
    x = [V[i].x for i in ans]
    y = [V[i].y for i in ans]
    axes.plot(x,y,color='y')
    
    poly = [[V[i].x,V[i].y] for i in ans]
    outpointid = []
    for i in range(pNum):
        if i not in ans and not isPoiWithinPoly([V[i].x,V[i].y],poly):
              outpointid.append(i)
    print(outpointid)
    for i in outpointid:
        distances = np.array([dis(V[i],V[j]) for j in ans])
        index = distances.argsort()[:2]
        first = max(index)
        second = min(index)
        print(ans[first],ans[second])
        
    plt.show()