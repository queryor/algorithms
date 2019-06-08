'''In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
'''
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # Runtime: 2520 ms, faster than 5.20% of Python3 online submissions for Can I Win.
        # Memory Usage: 17.6 MB, less than 96.43% of Python3 online submissions for Can I Win.
        candidate = [i for i in range(1,maxChoosableInteger+1)]
        flag = [1 for i in range(maxChoosableInteger)]
        dp = {}
        dp["".join([str(0) for i in range(maxChoosableInteger)])]=False
        return self.fun1(candidate,flag,desiredTotal,dp)
    
    def fun1(self,candidate,flag,target,dp)->bool:
        key  = "".join([str(i) for i in flag])
        #print(key)
        if key in dp:
            return dp[key]
        max_v = 0
        min_v = candidate[-1]
        res = 0
        for i,v in enumerate(candidate):
            if flag[i]==1:
                res+=v
                if v>max_v:
                    max_v=v
                if v<min_v:
                    min_v=v
        if target<=max_v:
            dp[key] = True
            return True
        elif min_v + max_v>=target or res<target:
            dp[key] = False
            return False
        for j,v in enumerate(candidate):
            if flag[j]==1:
                flag[j] = 0
                if self.fun1(candidate,flag.copy(),target-v,dp)==False:
                    dp[key]=True
                    return True
                flag[j] = 1
        dp[key]=False
        return False

    def canIWin1(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        candidate = [i for i in range(1,maxChoosableInteger+1)]
        return self.fun2(candidate,desiredTotal)
    def fun2(self,candidate,target)->bool:
        if sum(candidate)<target:
            return False
        if target<=max(candidate):
            return True
        elif min(candidate)+max(candidate)>=target:
            return False
        for j,v in enumerate(candidate):
            candidate.pop(j)
            if self.fun2(candidate.copy(),target-v)==False:
                return True
            candidate.insert(j,v)
        return False

s = Solution()
print(s.canIWin(5,50))
print(s.canIWin1(5,50))