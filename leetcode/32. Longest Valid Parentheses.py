# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        这里我们还是借助栈来求解，需要定义个start变量来记录合法括号串的起始位置，我们遍历字符串，
        如果遇到左括号，则将当前下标压入栈，如果遇到右括号，如果当前栈为空，则将下一个坐标位置记录到start，
        如果栈不为空，则将栈顶元素取出，此时若栈为空，则更新结果和i - start + 1中的较大值，
        否则更新结果和i - 栈顶元素中的较大值。
        '''
        t = []
        ans = 0
        start = 0 
        for i,c in enumerate(s):
            if len(t)==0 and c==')':
                start = i+1
                continue
            elif c=='(':
                t.append(i)
            elif c==')':
                t.pop()
                if len(t)==0:
                    ans = max(ans,i - start + 1)
                else: 
                    ans = max(ans,i-t[-1])
                    
        return ans
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dp = [0 for i in range(len(s)+1)]
        for i in range(1,len(s)+1):
            if s[i-1]=='(':
                dp[i]=0
            else: 
                j = i-2-dp[i-1]
                if s[j]==')' or j<0:
                    dp[i]=0
                else: 
                    dp[i]=dp[i-1]+2+dp[j]
            ans = max(ans,dp[i])
        return ans

s = Solution()
inputs = "(()))())("
#inputs = "(()"
#inputs = "()(())"
print(s.longestValidParentheses1(inputs))