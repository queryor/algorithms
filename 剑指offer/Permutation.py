# -*- coding:utf-8 -*-
# 题目描述
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return [ss]
        ret = []
        #遍历字符串，固定第一个元素，然后递归求解
        for i in range(len(ss)):
            for j in self.Permutation(ss[:i]+ss[i+1:]):
                ret.append(ss[i]+j)
        #通过set进行去重，sorted进行重新排序
        return sorted(list(set(ret))) 


s = 'aba'
a = Solution()
print(a.Permutation(s))