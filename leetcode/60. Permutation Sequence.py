# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note:

# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ### 因为n个字符的全排列是n!个，然后可以根据这个性质依次判定字符。注意要修改原字符
        ans = ""
        factorial = [1,1,2,6,24,120,720,5040,40320,362880,2628800]
        s = ""
        k -=1 #换成从0开始数的个数。
        for i in range(1,n+1):
            s+=str(i)        
        for i in range(n-1):
            c_num = n-i-1
            #print(k)
            index = k//factorial[c_num]+i
            ans+=s[index]
            k = k%factorial[c_num]
            s = s[:i]+s[index]+s[i:index]+s[index+1:] # 更改位置
            #print(index,ans,s)
        return ans+s[-1]
s = Solution()
n = 4
k = 9
print(s.getPermutation(4,9))