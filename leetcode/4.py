# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1,l2 = len(nums1),len(nums2)
        if l1==0 and l2 == 0:
            return False
        elif l1==0:
            s = nums2
        elif l2==0:
            s = nums1
        else:
            s = []
            i,j = 0,0
            while True:
                if nums1[i]<=nums2[j]:
                    s.append(nums1[i])
                    i+=1
                    if i == l1:
                        for c in nums2[j:l2]:
                            s.append(c)
                        break
                else:
                    s.append(nums2[j])
                    j+=1
                    if j == l2:
                        for c in nums1[i:l1]:
                            s.append(c)
                        break

        l = len(s)
        if l%2==0:
            return (s[l//2]+s[l//2-1])/2
        else:
            return float(s[l//2])
    def findMedianSortedArrays1(self, nums1, nums2):
        N1, N2= len(nums1), len(nums2)
        N = N1+N2
        i1, i2, i = 0,0,0
        prev = None
        cur = None
        
        while(i<N):
            if i1<N1 and i2<N2 and nums1[i1]<= nums2[i2]:
                cur  = nums1[i1]
                i1+=1
                
            elif i1<N1 and i2<N2 and nums1[i1]> nums2[i2]:
                cur = nums2[i2]
                i2+=1
            
            elif i1>=N1:
                cur = nums2[i2]
                i2+=1

            elif i2>=N2:
                cur = nums1[i1]
                i1+=1
            
            if N%2 ==1 and i == N//2: return cur
            elif N%2 ==0 and i == N//2: return 0.5*(cur+prev)
            prev = cur
            i+=1
            
        return 0


n1 = [1,2]
n2 = [3,4]
s = Solution()
print(s.findMedianSortedArrays1(n1,n2))