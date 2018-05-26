#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1740.py
@time: 2018/05/20
"""
# 描述
# 已知替换函数replace(c1, c2)的作用是把一个字符串中所有的c1字符替换成c2字符。  

# 请你判断能否使用replace函数将字符串S变成D。  

# 你可以调用replace函数任意多次。

# 输入
# 输入包含多组数据。  

# 第一行包含一个整数T，代表数据组数。  

# 每组数据包含两行，分别是字符串S和D。

# 1 ≤ T ≤ 10

# S和T都只包含小写字母，且1 ≤ |S| = |D| ≤ 1000

# 输出
# 对于每组数据输出YES或者NO，表示能否使用replace函数将字符串S变成D。




# 题解
# 生成一个字典转换表 然后依次转换
T = input()
for i in range(T):
    character = []
    for i in range(ord('a'),ord('z')+1):
        character.append(chr(i))
    dict = dict.fromkeys(character,0)
    # print dict
    s1 = raw_input()
    s2 = raw_input()
    if len(s1)!=len(s2):
        print 'NO'
        continue
    flag = True
    for i in range(len(s1)):
        if dict[s1[i]]==0:
            dict[s1[i]]=s2[i]
        elif dict[s1[i]]!=s2[i]:
            flag = False
    print 'YES' if flag else 'NO'    