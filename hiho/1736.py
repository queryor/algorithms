#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1736.py
@time: 2018/05/26
"""

# 描述
# 如果一个1~N的排列P=[P1, P2, ... PN]中的任意元素Pi都满足|Pi-i| ≤ K，我们就称P是K-偏差排列。

# 给定N和K，请你求出字典序最大的K-偏差排列。

# 注：字典序最大指首先P1应尽量大，其次P2尽量大，再次P3尽量大 …… 以此类推。

# 输入
# 包含两个整数N和K。  

# 对于50%的数据，1 ≤ N ≤ 10  

# 对于100%的数据，1 ≤ N ≤ 100, 1 ≤ K ≤ 100

# 输出
# 输出一行，包含一个1~N的排列，整数之间用一个空格隔开。

# 样例输入
# 5 2
# 样例输出
# 3 4 1 2 5





def fun(s,k,ans):
    if len(s)<k+1:
        s.reverse()
        for i in s:
            ans.append(i)
        # print ans1
        
    elif len(s)< 2*k+1:
        for i in s[k:]:
            ans.append(i)
        for i in s[:k]:
            ans.append(i )
    else:
        for i in s[k:2*k]:
            ans.append(i)   
        for i in s[:k]:
            ans.append(i )
        ans = fun(s[2*k:],k,ans)
    return ans

n,k = [int(i) for i in raw_input().split(' ')]

s = range(1,n+1)
ans = []
ans = fun(s,k,ans)
for i in ans[:-1]:
    print i,
print ans[-1]

