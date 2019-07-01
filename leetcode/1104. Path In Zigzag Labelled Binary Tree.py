'''In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6

'''

### Z 型的完全二叉树 给定一个值 到达该点的最短路径
## 找规律
import math
class Solution:
    def pathInZigZagTree(self, label: int):
        ans = []
        while label>=1:
            ans.insert(0,label)
            t = label//2
            n = math.floor(math.log2(label))
            res = 2**(n-1)+2**n-1-t
            label = res
        return ans
            
s = Solution()
label = 26
print(s.pathInZigZagTree(label))