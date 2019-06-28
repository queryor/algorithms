'''Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def findDuplicates(self, nums):
        n = len(nums)
        #print(n)
        nums = [i-1 for i in nums]
        for i in range(n):
            nums[nums[i]%n]+=n
        res = []
        #print(nums)
        for i in range(n):
            if nums[i]>=2*n:
                res.append(i+1)
        return res
s = Solution()
i = [10,2,5,10,9,1,1,4,3,7]
print(s.findDuplicates(i))
        