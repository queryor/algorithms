'''小明国庆节来北京玩，北京有N个景点，第 i 个景点的评分用a[i]表示，两个景点i, j之间的距离为j - i(j > i)。

小明一天只能游玩两个景点，我们认为总评分是两个景点的评分之和减去两个景点之间的距离，即为a[i]+a[j]+i-j。

那么小明选择哪两个景点才会总评分最大呢？

输入格式
第一行包含整数N。

第二行分别输入N个景点的评分。

输出格式
输出最大评分

数据范围
2≤N≤105,
1≤a[i]≤1000
输入样例：
5
11 6 5 18 12
输出样例：
29
'''

N = int(input().strip())
a = [int(i) for i in input().strip().split()]
## 方法1 暴力法
ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans = max(ans,a[j]+a[i]+i-j)
print(ans)

## a[i]+i 最大是固定的值 可以存下来
max_q = a[0]+0
ans = 0
for j in range(1,N):
    ans = max(ans,a[j]-j+max_q)
    max_q = max(max_q,a[j]+j)
print(ans)