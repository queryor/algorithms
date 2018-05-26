#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1745.py
@time: 2018/05/21
"""
#题目描述#
# 你有N张卡片，每张卡片上写着一个正整数Ai，并且N张卡片上的整数各不相同。  

# 此外，你还有M张百搭卡片，可以当作写着任意正整数的卡片。

# 一个“顺子”包含K张卡片，并且满足卡片上的整数恰好是连续的K个正整数。我们将其中最大的整数称作顺子的值。

# 例如1-2-3-4-5的值是5，101-102-103的值是103。  

# 请你计算用给定的N张卡片和M张百搭卡片，能凑出的值最大的顺子是多少，并且输出该顺子的值。

# 输入
# 第一行包含3个整数，N，M和K。  

# 第二行包含N个整数，A1, A2, ... AN。  

# 对于50%的数据，1 ≤ N, K ≤ 1000  

# 对于100%的数据，1 ≤ N, K ≤ 100000 0 ≤ M < K




# 题解

# 首先：要想最大，当然是把百变卡全用完。如果百变卡大于k-1那么直接在最大的那张牌往后变
# 否则，即使用完百变卡，仍需要k-m张牌才能凑齐一个顺子
# 因此首先找到手中从小到大连续的的k-m张牌（而且这些牌的跨度要小于等于k）
# 然后找出满足这个条件最大的情况，就能得到最大的顺子

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