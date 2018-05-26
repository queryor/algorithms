#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1744.py
@time: 2018/05/24
"""
# 题目描述
# 有一种叫作hohahola的饮料，售价是X元一瓶。小Hi非常喜欢这种饮料，但是他现在身无分文。

# 不过小Hi有N张优惠券，买hohahola时每瓶最多使用一张优惠券，可以使该瓶价格减少Y元。(Y ≤ X)  

# 同时优惠券可以出售，小Hi每出售一张优惠券可以获得Z元。  

# 请你帮小Hi计算通过出售若干优惠券，他最多可以买多少瓶hohahola。

# 输入
# 一行4个整数N, X, Y, Z。  

# 1 ≤ N, Z ≤ 1000000000 1 ≤ Y ≤ X ≤ 1000000000


# 题解
# 直接分情况计算

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