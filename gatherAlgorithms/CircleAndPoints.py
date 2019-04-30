# 固定半径的圆能覆盖的最多点数

import numpy as np
import matplotlib.pyplot as plt
import math

class interval:
    def __init__(self,arg=0,flag=False):
        self.arg = arg
        self.flag = flag
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def dis(a:point,b:point):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

# 画圆
def plot_circle(crd:point,r,axes,color='r'):
    #crd 圆心坐标
    # r  半径
    a,b = crd.x,crd.y
    theta = np.arange(0, 2*np.pi, 0.01)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)    
    axes.plot(x, y,color=color)
    axes.axis('equal')
def  get_max_circle(points,r):
    n = len(points)
    # float的精度考虑
    r+=0.0001
    ans = -1
    for i in range(n):
        event = []
        for j in range(n):
            if i == j:
                continue
            dist = dis(points[i],points[j])
            if dist<=2.0*r:
                cta = math.atan2(points[j].y-points[i].y,points[j].x-points[i].x)
                if cta<0:
                    cta+=2*math.pi
                delta = math.acos(dist/2/r)
                a1 = cta - delta
                a2 = cta + delta
                if a1<0:
                    event.append(interval(arg=a1+2*math.pi,flag=True))
                    event.append(interval(arg=a2+2*math.pi,flag=False))
                else:
                    event.append(interval(arg=a1,flag=True))
                    event.append(interval(arg=a2,flag=False))
                    event.append(interval(arg=a1+2*math.pi,flag=True))
                    event.append(interval(arg=a2+2*math.pi,flag=False))
        if len(event)<ans:
            continue
        event.sort(key=lambda x:x.arg)
        #print([x.arg for x in event]) 
        res = 0
        for j in range(len(event)):
            if event[j].flag:
                res+=1
            else: 
                res-=1
            if res>ans:
                ans = res
                center_id = i
                center_arg = event[j].arg
    print(ans)
    p = points[center_id] 
    x = p.x + r*math.cos(center_arg)
    y = p.y + r*math.sin(center_arg)
    return point(x,y),ans+1   
    
if __name__ == "__main__":
    #画图初始化
    fig = plt.figure() 
    axes = fig.add_subplot(1,1,1)
    ##固定半径
    r = 2
    #初始化点坐标
    x = [1,2,3,4,5,6,7]
    y = [2,4,7,4,5,8,1]
    axes.scatter(x,y)
    points = [point(x[i],y[i]) for i in range(len(x))]
    #画出原始圆
    for p in points:
        plot_circle(p,r,axes)

    ## 得到覆盖点最多的圆的圆心
    centerPoint,counter = get_max_circle(points,r)
    plot_circle(centerPoint,r,axes,color='b')
    #显示图
    plt.show()
    
    
