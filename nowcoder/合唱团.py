import sys
n=int(sys.stdin.readline().strip())
a=list(map(int,sys.stdin.readline().split()))
k,d=list(map(int,sys.stdin.readline().split()))
##fm 最大 fm最小
fm = [[0 for i in range(n)]for i in range(k+1)]
fn = [[0 for i in range(n)]for i in range(k+1)]
ans = -float('inf')
for i in range(n):
    fm[1][i]=fn[1][i]=a[i]
    for k_it in range(2,k+1):
        for j in range(i-1,max(i-d,0)-1,-1):
            fm[k_it][i]=max(fm[k_it][i],max(fm[k_it-1][j]*a[i],fn[k_it-1][j]*a[i]))
            fn[k_it][i]=min(fn[k_it][i],min(fm[k_it-1][j]*a[i],fn[k_it-1][j]*a[i]))
    ans = max(ans,fm[k][i])
print(ans)