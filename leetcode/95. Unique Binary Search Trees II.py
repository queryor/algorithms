# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:

# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 二叉搜索树的生成
# 一看就是使用递归
class Solution:
    def generateTrees(self, n: int):
        if n==0:
            return []
        nums = [i+1 for i in range(n)]
        return self.generateTreesDFS(nums)

    
    def generateTreesDFS(self,nums):
        ans = []
        if len(nums)==0:
            ans.append(None)
        elif len(nums)==1:
            ans.append(TreeNode(nums[0]))
        else:
            for i in range(len(nums)):
                left= self.generateTreesDFS(nums[:i])
                right= self.generateTreesDFS(nums[i+1:])
                for l in left:
                    for r in right:
                        NewNode = TreeNode(nums[i])
                        NewNode.left = l
                        NewNode.right = r
                        ans.append(NewNode)
        return ans


        