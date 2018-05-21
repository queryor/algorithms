#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1745.py
@time: 2018/05/21
"""

s = raw_input()
# print s.split(' ')
n,m,k = s.split(' ')[:3]
n = int(n)
m = int(m)
k = int(k)

s = raw_input()
s = s.split(' ')
s = [int(i) for i in s]
s.sort()
ans = 0
# table = [1 for n in range(0,s[-1]+1)]
# for i in s:
#     table[i] = 0 
# for i in range(s[-1],-1,-1):
#     if(sum(table[i-k+1:i+1])<=m):
#         ans = i
#         break
#     else:
#         pass
# print ans
if k-m<=1:
    ans = s[-1]+m
else:
    for i in range(len(s)):
        if(i+k-m-1<n):
            if s[i+k-m-1]-s[i]+1<=k:
                ans = s[i]+k-1

print ans