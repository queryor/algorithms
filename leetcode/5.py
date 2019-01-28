# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        max_s = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if self.isPalind(s[i:j]):
                    if j-i >max_s:
                        out = s[i:j]
                        max_s = j-i
        return out
    def isPalind(self,s):
        if len(s)==0:
            return True
        else:
            for i in range(len(s)//2):
                if s[i]!=s[-i-1]:
                    return False
        return True

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        out = ""
        max_n = 0
        for i in range(len(s)):
            j = 0
            while(i-j>=0 and i+j<len(s)):
                if(s[i-j]==s[i+j]):
                    l = 2*j+1
                    if(l>max_n):
                        max_n = l
                        out = s[i-j:i+j+1]
                else:
                    break
                j+=1
            if i+1<len(s) and s[i] == s[i+1]:
                j = 0
                while(i-j>=0 and i+j+1<len(s)):
                    if(s[i-j]==s[i+j+1]):
                        l = 2*j+2
                        if(l>max_n):
                            max_n = l
                            out = s[i-j:i+j+2]
                    else:
                        break
                    j+=1

        return out

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        out = ""
        max_n = 0
        for i in range(len(s)):
            j = 0
            while(i-j>=0 and i+j<len(s)):
                if(s[i-j]!=s[i+j]):
                    break
                j+=1
            j = j-1
            l = 2*j + 1
            if l > max_n:
                max_n = l
                out = s[i-j:i+j+1]
                #print(i,j,out)
            if i+1<len(s) and s[i] == s[i+1]:
                j = 0
                while(i-j>=0 and i+j+1<len(s)):
                    if(s[i-j]!=s[i+j+1]):
                        break
                    j+=1
                j = j-1
                l = 2*j + 2
                if l > max_n:
                    max_n = l
                    out = s[i-j:i+j+2]

        return out
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            if i<R:
                P[i]=min(P[2*C - i],R-i )
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1 
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
            if R == '#':
                break
            
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
	
		#change the last part to get 120 ms, faster than 94.87% :
		
		        # Find the maximum element in P.
        #maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        maxLen = max(P)
        centerIndex = P.index(maxLen)
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

s1 = "cbbd"
s = Solution()
print(s.longestPalindrome3(s1))