# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return(haystack.find(needle))
    def strStr1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.KMP(haystack,needle)
    def KMP(self,t,p):
        i = 0
        j = 0
        if len(t)==0 and len(p)==0:
            return 0
        elif len(t)==0 or len(p)==0:
            return -1
        Next = self.getNext(p)
        while i<len(t) and j < len(p):
            if j == -1 or t[i]==p[j]:
                i+=1
                j+=1
            else: 
                j = Next[j]

        if j == len(p):
            return i - j
        else: 
            return -1

    
    def  getNext(self,p):
        l = len(p)
        Next = [0 for i in range(l)]
        Next[0]=-1
        j = 0
        k = -1
        while j < l-1:
            if k==-1 or p[j]==p[k]:
                k+=1
                j+=1
                if(p[j]==p[k]):
                    Next[j]=Next[k]
                else: 
                    Next[j] = k
            else: 
                k = Next[k]
        

        return Next

s = Solution()
haystack = "hello"
needle = "ll"
print(s.strStr1(haystack,needle))
                