'''一个强密码应满足以下所有条件：

由至少6个，至多20个字符组成。
至少包含一个小写字母，一个大写字母，和一个数字。
同一字符不能连续出现三次 (比如 "...aaa..." 是不允许的, 但是 "...aa...a..." 是可以的)。
编写函数 strongPasswordChecker(s)，s 代表输入字符串，如果 s 已经符合强密码条件，则返回0；否则返回要将 s 修改为满足强密码条件的字符串所需要进行修改的最小步数。

插入、删除、替换任一字符都算作一次修改。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strong-password-checker
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        s1,s2,s3=0,0,0
        for c in s:
            if c.isupper():
                s2=1
            if c.islower():
                s1=1
            if c.isdigit():
                s3=1
        n = len(s)
        if n==0:
            return 6
        pre = s[0]
        cnt = 1
        res = 0
        re = 0
        add = 0
        List = []
        for i in range(1,n):
            if s[i]==pre:
                cnt+=1
                if i==n-1:
                    if cnt>=3:
                        res+=cnt//3
                        List.append(cnt)
            else:
                if cnt>=3:
                    res+=cnt//3
                    List.append(cnt)
                pre = s[i]
                cnt = 1
        if n<6:
            add=6-n
        if n>20:
            re=n-20
        if add == 0 and re==0 and res==0 and s1==1 and s2==1 and s3==1:
            return 0
        if re==0 and add==0:
            if res>=2:
                return res
            if (s3==0 and(s1==0 or s2==0)):
                return max(res,2)
            if s1==0 or s2==0 or s3==0:
                return max(res,1)
            else:
                return res
        elif add!=0:
            print(s1,s2,s3)
            if add>=2:
                return add
            if (s3==0 and(s1==0 or s2==0)):
                return 2
            if s1==0 or s2==0 or s3==0:
                return 1
            else:
                return 1
        else:
            if res==0:
                if (s3==0 and(s1==0 or s2==0)):
                    return re+2
                if s1==0 or s2==0 or s3==0:
                    return re+1
                else:
                    return re
            else:
                List.sort()
                #print(List)
                res = 0
                rm = 0
                for i in range(len(List)):
                    if re>0:
                        while List[i]>2 and re>0:
                            if re>=List[i]%3+1:
                                re-=List[i]%3+1
                                rm+=List[i]%3+1
                                List[i]-=List[i]%3+1
                                
                            else:
                                break
                        res+=List[i]//3
                    else:
                        res+=List[i]//3
                #print(List)
                if res>=2:
                    return res+rm+re
                if (s3==0 and(s1==0 or s2==0)):
                    return max(res,2)+rm+re
                if s1==0 or s2==0 or s3==0:
                    return max(res,1)+rm+re
                else:
                    return res+re+rm
                
s = Solution()
i = "aaaaaaaAAAAAA6666bbbbaaaaaaABBC"
print(s.strongPasswordChecker(i))