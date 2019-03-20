# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ## 主要判断左右孩子是不是叶子节点
        return self.getminDepth(root)
    def getminDepth(self,root):
        if root ==None:
            return 0
        if root.left == None and root.right==None:
            return 1
        elif root.left == None:
            return self.getminDepth(root.right)+1
        elif root.right==None:
            return self.getminDepth(root.left)+1
        return 1+min(self.getminDepth(root.left),self.getminDepth(root.right))