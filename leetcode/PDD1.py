
def fun(a,b):
    n = len(a)
    index = []
    for i in range(n):
        if i ==0 and a[i]>=a[i+1]:
            index.append(i)
        elif i == n-1 and a[i]<=a[i-1]:
            index.append(i)
        elif i!=0 and i!=n-1:
            if a[i]<=a[i-1] or  a[i]>=a[i+1]:
                index.append(i)
    print(index)
    flag = 0
    for i in range(len(index)-1,-1,-1):
        ind = index[i]
        res = a[ind]
        for j in range(len(b)):
            if ind != 0 and ind!=n-1 and b[j]>a[ind-1] and b[j]<a[ind+1]:
                res = max(res,b[j])
            elif ind ==0 and b[j]<a[ind+1]:
                res = max(res,b[j])
            elif ind == n-1 and b[j]>a[ind-1]:
                res = max(res,b[j])
        if res !=a[ind]:
            a[ind] = res
            flag = 1
            break
    if flag == 1:
        return a
    else:
        return None

if __name__ == "__main__":
    a = [int(i) for i in input().strip().split()]
    b = [int(i) for i in input().strip().split()]
    res = fun(a,b)
    if res !=None:
        print(res)
    else:
        print("NO")