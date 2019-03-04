# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        inputs = sorted(nums)
        ans = []
        self.get_all_arrange("",inputs,ans)
        str1 = ""
        for i in nums:
            str1 = str1+str(i)
        for i,s in enumerate(ans):
            if s == str1:
                result = ans[(i+1)%len(ans)]    
        for i,c in enumerate(result):
            nums[i]=int(c)

    def get_all_arrange(self,p,s,ans):
        if len(s)==0:
            return ans.append(p)
        if len(s)==1:
            return ans.append(p+str(s[0]))
        #s = s.sort()
        for i,c in enumerate(s):
            self.get_all_arrange(p+str(c),s[:i]+s[i+1:],ans)

    def nextPermutation1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in range(len(nums)-1,0,-1):
            if(nums[i]>nums[i-1]):
                flag=1
                for j in range(len(nums)-1,0,-1):
                    if nums[j]>nums[i-1]:
                        t = nums[i-1]
                        nums[i-1] = nums[j]
                        nums[j] = t
                        break
                nums[i:] = nums[len(nums)-1:i-1:-1]
                break
        #print(flag,nums)
        if flag == 0:
            nums[::] = nums[::-1]
            #或者nums.reverse()
            #print(nums)

s = Solution()
ans = []
inputs = [3,2,1]
s.nextPermutation1(inputs)
print(inputs)
#print(ans)
