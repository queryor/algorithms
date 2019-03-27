# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Example 1:

# Input: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# Output: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# Example 2:

# Input: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# Output: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# Follow up:

# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 对于此问题，关键是要找到被调换的两个元素。我们知道，对于中序遍历，合法的BST数必为有序，故进行中序遍历，
        # 如果pre.val >root.val说明有误。注意区分第一次和第二次，标记即可
        self.pre,self.first,self.second=None,None,None
        self.dfs(root)
        t=self.first.val
        self.first.val,self.second.val = self.second.val,t
 
    def dfs(self,root):
        if not root: return
        if root.left:  self.dfs(root.left)
        
        if self.pre:
            if self.pre.val > root.val : 
                if not self.first :self.first,self.second=self.pre,root
                else:   self.second=root
 
        self.pre=root
        if root.right: self.dfs(root.right)