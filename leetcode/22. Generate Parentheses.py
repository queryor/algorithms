# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self.generateParenthesisDFS(n,n,"",res)
        return res
    def generateParenthesisDFS(self,left,right,out,res):
        if(left>right):
            return 0
        if left == 0 and right == 0:
            res.append(out)
        else: 
            if(left>0):
                self.generateParenthesisDFS(left-1,right,out+'(',res)
            if(right>0):
                self.generateParenthesisDFS(left,right-1,out+')',res)





s  = Solution()
a = 3
print(s.generateParenthesis(3))