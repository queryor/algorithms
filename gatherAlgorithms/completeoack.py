w = [150,200,350]
c = [150,200,350]
V = 855

N = len(w)
dp = [0 for i in range(V+1)]
for i in range(0,N):
    for v in range(c[i],V+1):
        dp[v]=max(dp[v],dp[v-c[i]]+w[i])
print(V-dp[-1])