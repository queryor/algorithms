'''（这是一个 交互式问题 ）

给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

如果不存在这样的下标 index，就请返回 -1。

 

所谓山脉数组，即数组 A 假如是一个山脉数组的话，需要满足如下条件：

首先，A.length >= 3

其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

你将 不能直接访问该山脉数组，必须通过 MountainArray 接口来获取数据：

MountainArray.get(k) - 会返回数组中索引为k 的元素（下标从 0 开始）
MountainArray.length() - 会返回该数组的长度
 

注意：

对 MountainArray.get 发起超过 100 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

为了帮助大家更好地理解交互式问题，我们准备了一个样例 “答案”：https://leetcode-cn.com/playground/RKhe3ave，请注意这 不是一个正确答案。

 

示例 1：

输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
示例 2：

输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。
'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
'''题意：告诉一个山峰数组，问一个目标数字是否在山峰里，如果存在，输出最小的下标。

思路：山峰是一个先递增再递减的数组。
如果可以找到最高点的下标，则可以现在左半部二分查找，找到了则返回答案。
没找到再去右半部二分查找，找到了则找到，没找到则不存在目标。

这里查找最高点有两个方法。
第一个方法是传统的三分查找。
第二个方法是二分查找加特殊判断（判断当前属于递增区间还是递减区间）。

而递增二分查找与递减二分查找是对称的，所以两个代码也可以合并为一个代码，使用flag标记即可。
'''


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = self.findpeak(mountain_arr)
        #print(peak)
        left = self.findbinary(target,mountain_arr,0,peak,0)
        if left!=None:
            return left
        right = self.findbinary(target,mountain_arr,peak+1,mountain_arr.length()-1,1)
        if right!=None:
            return right
        return -1
    
    def findpeak(self,m):
        n = m.length()
        left = 1
        right = n-1
        while left<right:
            mid = (right+left)//2
            val = m.get(mid)
            pre = m.get(mid-1)
            last = m.get(mid+1)
            if val>pre and val>last:
                return mid
            if val<last:
                left = mid+1
            else: 
                right = mid-1
        return left

    def findbinary(self,target,m,start,end,dire=0):# dire 0：升序 1：降序
        preval = m.get(start)
        #print(start,end)
        if preval == target:
            return start
        if start>=end:
            return None
        nextval = m.get(end)
        if nextval==target:
            return end
        mid = (start+end)//2
        midval = m.get(mid)
        if midval == target:
            return mid
        if (midval <target and dire==0) or (midval>target and dire==1):
            return self.findbinary(target,m,mid+1,end,dire)
        else: 
            return self.findbinary(target,m,start,mid-1,dire)
