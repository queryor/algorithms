# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# Example:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]

class Solution:
    def restoreIpAddresses(self, s: str):
        ## DFS
        ans = []
        def IpDFS(s,index,k,res=[]):
            if k == 0 and index==len(s):
                ans.append('.'.join(res))
                #print(ans)
            elif len(s)<4:
                pass
            elif len(s)==k:
                ans.append('.'.join(s))
            elif len(s[index:])>3*k or len(s[index:])<k:
                pass
            else: 
                for i in range(1,4):
                    if index+i>len(s):
                         continue
                    n=int(s[index:index+i])
                    t_s = s[index:index+i]
                    ### 注意处理每个数字不能出现以0开头的数字
                    if len(t_s)!=1 and t_s[0]=='0':
                        break
                    if n>=0 and n<=255:
                        res.append(s[index:index+i])
                        IpDFS(s,index+i,k-1,res)
                        res.pop()
        res = []
        IpDFS(s,0,4,res)
        return ans
            



s = Solution()
i = "25525511135"
i = "010010"

print(s.restoreIpAddresses(i))