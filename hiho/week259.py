'''时间限制:10000ms
单点时限:1000ms
内存限制:256MB
描述
小Hi写程序时习惯用蛇形命名法(snake case)为变量起名字，即用下划线将单词连接起来，例如：file_name、 line_number。  

小Ho写程序时习惯用驼峰命名法(camel case)为变量起名字，即第一个单词首字母小写，后面单词首字母大写，例如：fileName、lineNumber。  

为了风格统一，他们决定邀请公正的第三方来编写一个转换程序，可以把一种命名法的变量名转换为另一种命名法的变量名。

你能帮助他们解决这一难题吗？

输入
第一行包含一个整数N，表示测试数据的组数。(1 <= N <= 10)    

以下N行每行包含一个以某种命名法命名的变量名，长度不超过100。

输入保证组成变量名的单词只包含小写字母。

输出
对于每组数据，输出使用另一种命名法时对应的变量名。

样例输入
2  
file_name  
lineNumber 
样例输出
fileName  
line_number
'''

n = int(input().strip())
for i in range(n):
    s = input().strip()
    if '_' in s:
        j = 0
        while(j<len(s)):
            if s[j]=='_':
                s = s[:j]+s[j+1:j+2].upper()+s[j+2:]
            j+=1
        print(s)
    else: 
        j = 0
        while(j<len(s)):
            if s[j].isupper():
                s = s[:j]+'_'+s[j].lower()+s[j+1:]
            j+=1
        print(s)
        