'''
给定若干个数 加四则运算括号使得等于目标数
初步给4个数
'''
exp = ['+','-','*','/']
def fun(a,target):
    n = len(a)
    a = [str(i) for i in a]
    res = []
    ans = []
    dfs(res,ans,0,n-1)
    #print(res)
    for r in res:
        s = []
        for i in range(n-1):
            s.append(a[i])
            s.append(r[i])
        s.append(a[-1])
        #print(s)
        #print(s,eval(''.join(s)))
        dfs2(s,target)
        #break
def dfs(res,ans,i,n):
    if i==n:
        res.append(ans)
        return
    for c in exp:
        ans.append(c)
        dfs(res,ans.copy(),i+1,n)
        ans.pop()
def dfs2(s,target,res=[]):
    n = len(s)
    if n ==1:
        #print(s)
        try: 
            ans = eval(s[0])
            #print(ans)
        except:
            return
        else:
            if ans==target:
                print(s[0])
            return
    for i in range(0,n,2):
        for j in range(i+2,n,2):
            t = s[:i] + ['('+str("".join(s[i:j+1]))+')']+s[j+1:]
            #t = s[:i] + [str(eval("".join(s[i:j+1])))]+s[j+1:]
            dfs2(t,target)

a = [1,3,5,7]
target = -1
print(fun(a,target))