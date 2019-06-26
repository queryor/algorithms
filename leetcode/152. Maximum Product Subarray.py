'''给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
## 参考题解
'''
此题与53题类似，不同处是53题的运算是加法，本题是乘法。
对于加法，在遍历数组中始终取max(ma + nums[i], nums[i])即可，因为无论nums[i]的正负如何，
对与乘法，在遍历数组中，若nums[i]是负数，那么当前最大值ma * nums[i]会变成当前最小值（负数），因此不能简单的只记录最大值。
本题的解题思路是同时记录当前最大值和最小值ma, mi：
当nums[i]是正数时，ma, mi * nums[i]仍然是最大值，最小值；
当nums[i]是负数时，ma, mi * nums[i]将变成最小值， 最大值；
因此，当nums[i] < 0时，我们交换ma, mi。
在遍历nums过程中，每次更新res获取全局最大值。

链接：https://leetcode-cn.com/problems/two-sum/solution/maximum-product-subarray-dong-tai-gui-hua-by-jin40/
'''

class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        if n==0:
            return
        ma,mi = nums[0],nums[0]
        res = nums[0]
        for i in range(1,n):
            if nums[i]>0:
                ma,mi = max(nums[i],ma*nums[i]),min(nums[i],mi*nums[i])
            else:
                ma,mi = max(nums[i],mi*nums[i]),min(nums[i],ma*nums[i])
            res = max(ma,res)
        return res
s = Solution()
i = [0,2]
print(s.maxProduct(i))