'''
亚历克斯和李继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。

亚历克斯和李轮流进行，亚历克斯先开始。最初，M = 1。

在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。

游戏一直持续到所有石子都被拿走。

假设亚历克斯和李都发挥出最佳水平，返回亚历克斯可以得到的最大数量的石头

'''

# 输入：piles = [2,7,9,4,4]
# 输出：10
# 解释：
# 如果亚历克斯在开始时拿走一堆石子，李拿走两堆，接着亚历克斯也拿走两堆。在这种情况下，亚历克斯可以拿到 2 + 4 + 4 = 10 颗石子。 
# 如果亚历克斯在开始时拿走两堆石子，那么李就可以拿走剩下全部三堆石子。在这种情况下，亚历克斯可以拿到 2 + 7 = 9 颗石子。
# 所以我们返回更大的 10。 


# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4

class Solution:
    def stoneGameII(self, piles) -> int:
        n = len(piles)
        dp = [[0 for i in range(n+1)] for i in range(n+1)]
        s = [0 for i in range(n+1)]
        for i in range(1,n+1):
            s[i] = s[i-1]+piles[i-1]
        for i in range(n,0,-1):
            for j in range(n+1):
                k = 1 
                while k<=2*j and i+k-1<n:
                    #print(i,j,k)
                    dp[i][j] = max(dp[i][j],s[n]-s[i-1]-dp[i+k][min(n,max(j,k))])
                    k+=1
        return dp[1][1]



s = Solution()
p = [2,7,9,4,4]
print(s.stoneGameII(p))