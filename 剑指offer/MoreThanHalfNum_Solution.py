# 题目描述
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

# 解题思路
# 用个字典统计每个数的频数

# 更好的解题思路



# 方法一：采用用户“分形叶”思路（注意到目标数 超过数组长度的一半，对数组同时去掉两个不同的数字，到最后剩下的一个数就是该数字。
# 如果剩下两个，那么这两个也是一样的，就是结果），
# 在其基础上把最后剩下的一个数字或者两个回到原来数组中，将数组遍历一遍统计一下数字出现次数进行最终判断。

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        count = {}
        for n in numbers:
            n = str(n)
            if count.has_key(n):
                count[n]+=1
            else:
                count[n]=1
        flag = 0
        for k,v in count.items():
            if v>len(numbers)/2:
                return(int(k))
        return 0

s = [1,2,3]
a = Solution()
print a.MoreThanHalfNum_Solution(s)