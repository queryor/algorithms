'''Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

class Solution:
    def singleNumber(self, nums) -> int:
        #直接异或
        ans = 0
        for num in nums:
            ans^=num
        return ans
    def singleNumber1(self, nums) -> int:
        #set
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.remove(num)
        return s.pop()


Input= [4,1,2,1,2]
s = Solution()
print(s.singleNumber1(Input))