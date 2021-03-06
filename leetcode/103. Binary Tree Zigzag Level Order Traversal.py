# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution:
    def zigzagLevelOrder(self,root:TreeNode):
        ## 使用两个队列 
        if root == None:
            return []
        q = []
        q.append(root)
        res = []
        ans = []
        flag = 1
        while len(q)!=0:
            n = len(q)
            new_q = []
            for i in range(n):
                node = q[i]
                ans.append(node.val)
                if node.left!=None:
                    new_q.append(node.left)
                if node.right!=None:
                    new_q.append(node.right)
            if flag == -1:
                ans = ans[::-1]
            flag = -flag
            res.append(ans)
            ans=[]
            q = new_q
        return res 
    
        