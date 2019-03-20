# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
## 把 102 题的结果翻转一下

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        # 递归 recursion
        s = []
        if root == None:
            return s
        s.append(root)
        res = []
        self.levelOrderDFS(s,res)
        return res[::-1]

    def levelOrderDFS(self,s,res):
        if len(s)==0:
            return 0
        else:
            ans = []
            new_s = []
            for node in s:
                ans.append(node.val)
                if node.left!=None:
                    new_s.append(node.left)
                if node.right!=None:
                    new_s.append(node.right)
            res.append(ans)
            self.levelOrderDFS(new_s,res)
            