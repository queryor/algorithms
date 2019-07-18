''''给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
注意：

你可以假设 k 总是有效的，1 ≤ k ≤ 输入数组的大小，且输入数组不为空。

进阶：

你能在线性时间复杂度内解决此题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
''''
### 简单解法直接暴力 O(kn)
### 使用队列 O(n) 方法参考 程序员代码面试指南
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        res = []
        if len(nums)==0 or k<1 or len(nums)<k:
            return res
        q = []
        n = len(nums)
        for i in range(n):
            while len(q)!=0 and nums[q[-1]]<=nums[i]:
                q.pop(-1)
            q.append(i)
            ### 去除队首元素
            if q[0] == i-k:
                q.pop(0)
            if i>=k-1:
                res.append(nums[q[0]])
        return res