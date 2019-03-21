# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res = []
        ans = []
        self.pathSumDFS(root,sum,ans,res)
        return res    
    def pathSumDFS(self,root,target,ans,res):
        if root == None:
            return 0
        ans.append(root.val)
        if root.val == target and root.left == None and root.right ==None:
            res.append(ans.copy())
        self.pathSumDFS(root.left,target-root.val,ans.copy(),res)
        self.pathSumDFS(root.right,target-root.val,ans.copy(),res)
        ans.pop()
 