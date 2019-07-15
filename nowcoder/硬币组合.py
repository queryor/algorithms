'''
3. 三种面值货币1元，2元和5元，有多少种方法组合成100元？有哪些组合方法？证明方法的正确性？
'''


'''
dp[i][sum] = 用前i种硬币构成sum 的所有组合数
那么题目的问题实际上就是求dp[m][sum]，即用前m种硬币（所有硬币）构成sum的所有组合数。在上面的联合等式中：当xn=0时，有多少种组合呢？ 
实际上就是前i-1种硬币组合sum，有dp[i-1][sum]种！ xn = 1 时呢，有多少种组合？ 实际上是用前i-1种硬币组合成(sum - Vm)的组合数，有dp[i-1][sum -Vm]种; xn =2呢， dp[i-1][sum - 2 * Vm]种，等等。
所有的这些情况加起来就是我们的dp[i][sum]。所以：

dp[i][sum] = dp[i-1][sum - 0*Vm] + dp[i-1][sum - 1*Vm]

+ dp[i-1][sum - 2*Vm] + ... + dp[i-1][sum - K*Vm]; 其中K = sum / Vm
'''
def fun(n,s):
    coins = [1,2,5]
    dp=[0]*100001
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i],n+1):
            dp[j] = dp[j]+dp[j-coins[i]]
    
    return dp[n]
        
s = {}
print(fun(3,s))