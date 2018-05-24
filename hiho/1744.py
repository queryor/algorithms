#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1744.py
@time: 2018/05/24
"""

s  = raw_input()
n,x,y,z = [int(i) for i in s.split(' ')]
ans = 0
w = 0
if z>y:
    ans = z*n/x
elif x==y:
    ans = n
else:
    ans=n*z/(x-y+z)
print ans