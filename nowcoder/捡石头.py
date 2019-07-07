import sys
def fun1(a,s,n,start):
    if "{}_{}".format(n,start) in s:
        return s["{}_{}".format(n,start)]
    if start>len(a):
        return 0
    if n+start>=len(a):
        return sum(a[start:]),len(a),len(a)-start
    res = 0
    take = 0
    for i in range(1,n+1):
        t = sum(a[start:start+i])
        t_m,s2,take_num = fun1(a,s,2*i,start+i)
        #print(n,start,i,t,t_m,s2,take_num)
        if t+sum(a[start+i:])-t_m>res:
            res=t+sum(a[start+i:])-t_m
            take = i
    s["{}_{}".format(n,start)] = res
    return res,start+take,take
    
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline().strip()))
    s = {}
    print(fun1(a,s,2,0)[0])