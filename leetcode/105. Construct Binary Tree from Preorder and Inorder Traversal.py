# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Accepted
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if preorder==[] or inorder==[]:
            return None
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                break
        cur = TreeNode(preorder[0])
        cur.left = self.buildTree(preorder[1:1+i],inorder[:i])
        cur.right = self.buildTree(preorder[1+i:],inorder[i+1:])
        return cur
        