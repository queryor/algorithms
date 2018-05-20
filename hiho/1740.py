#!/usr/bin/env python
# coding=utf-8
"""
@author:queryor
@file: 1740.py
@time: 2018/05/20
"""


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