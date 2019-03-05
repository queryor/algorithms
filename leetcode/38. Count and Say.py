# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n<1 and n>30:
            return None
        if n == 1:
            return "1"
        pr = "1"
        for i in range(2,n+1):
            print(pr)
            res = ""
            j=0
            while j<len(pr):
                cnt = 1
                while(j+1<len(pr) and pr[j+1]==pr[j]):
                    cnt+=1
                    j+=1
                res = res + str(cnt)+pr[j]
                j+=1
            pr = res
        return pr

s = Solution()
i = 5
print(s.countAndSay(i))