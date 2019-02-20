# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        j = -1
        flag = 0
        ans = []
        if numRows==1:
            return s
        for i in range(numRows):
            print(i)
            ans.append([])
        for i in range(len(s)):
            if (flag==0):
                j += 1
                if j==numRows-1:
                    flag = 1
            else:
                j -= 1
                if j == 0:
                    flag = 0
            #print(j)
            ans[j].append(s[i])
        ans = [y for x in ans for y in x]
        return ''.join(ans)

s  = Solution()
a = "ABCDEF"
print(s.convert(a,2))