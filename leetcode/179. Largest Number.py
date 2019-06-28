'''给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import functools
class Solution:
    def largestNumber(self, nums) -> str:
        def mycmp(n1,n2):
            if str(n1)+str(n2)>str(n2)+str(n1):
                return 1
            elif str(n2)+str(n1)>str(n1)+str(n2):
                return -1
            else:
                return 0
        nums = sorted(nums,key=functools.cmp_to_key(mycmp),reverse=True)
        return str(int(''.join([str(i) for i in nums])))

s = Solution()
i = [3,30,34,5,9]
print(s.largestNumber(i))
