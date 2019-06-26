'''给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def maximumGap(self, nums) -> int:
        # 桶排序
        # 参考：https://blog.csdn.net/zxzxzx0119/article/details/82889998
        # 设置n+1个桶是为了保证间距最大的两个数被分到不同的桶中
        # 因为最大间距 x >= (max_val - min_val) / (n-1)
        # 而使用n+1个桶每个桶中数的差值最大为 (max_val - min_val) / n 因此一个桶不可能同时存放间距最大的两个数
        if len(nums) < 2:
            return 0
        min_val, max_val, n = float('inf'), float('-inf'), len(nums)
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
            if nums[i] > max_val:
                max_val = nums[i]

        if min_val == max_val:
            return 0

        mins = [0] * (n + 1)
        maxs = [0] * (n + 1)
        has_num = [False] * (n + 1)

        for num in nums:
            index = int((num - min_val) * n / (max_val - min_val))
            mins[index] = num if not has_num[index] else min(mins[index], num)
            maxs[index] = num if not has_num[index] else max(maxs[index], num)
            has_num[index] = True

        max_len = 0
        m = maxs[0]
        for i in range(1, n + 1):
            if has_num[i]:
                curr_len = mins[i] - m
                if curr_len > max_len:
                    max_len = curr_len
                m = maxs[i]

        return max_len

