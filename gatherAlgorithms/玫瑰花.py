'''有K种不同的玫瑰花，现在要摆放在N个位置上，要求每种颜色的花至少出现过一次，请问有多少种不同的方案数呢？，因为答案可能很大，你只需要输出它对772235取余后的结果.


输入描述:
输入只有1行，分别有两个整数N,K( 1 <= N <= 50000 , 1 <= K <= 30 )

输出描述:
输出一行表示答案

输入例子1:
3 2

输出例子1:
6
'''

def fun(k,n): ### K 种花 无限取 求出取出总共为n种花的分布情况
    res = [0]
    t = math.factorial(n+k)%772235
    help(k,0,n,res,t)
    return res[0]
def help(k,s,n,res,t,ans=[]):
        if s == k-1:
            ans.append(n)
            t_ans = t
            for i in ans.copy():
                t_ans  = t_ans/(math.factorial(i+1)%772235)
            res[0]+=int(t_ans)%772235
            #print(res)
            ans.pop()
            return
        for i in range(n+1):
            ans.append(i)
            help(k,s+1,n-i,res,t,ans)
            ans.pop()
import math

### dp 不会做 遇到就放弃
if __name__ == "__main__":
    ans = 0
    n,k = [int(x) for x in input().strip().split()]
    value=[i+1 for i in range(k)]
    for j in range(1,k):
        key=[i+1 for i in range(value[j])]
        sum_=0
        for i in range(j):
            key[i]=math.factorial(value[j])/(math.factorial(value[j]-key[i])*math.factorial(key[i]))
            temp1 = key[i]*value[i]%772235
            sum_+=temp1
            sum_=sum_%772235
        temp2 = pow(value[j],n)%772235
        value[j]=int((temp2-sum_)%772235)
    print(value[k-1])
