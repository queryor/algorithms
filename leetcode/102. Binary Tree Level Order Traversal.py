# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
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
    def levelOrder(self, root: TreeNode):
        ## 使用两个队列 
        q = queue.Queue()
        q1 = queue.Queue()
        q.put(root)
        res = []
        ans = []
        while q.qsize()!=0 or q1.qsize()!=0:
            if q.qsize()!=0:
                node = q.get()
                if node == None:
                    continue
                ans.append(node.val)
                q1.put(node.left)
                q1.put(node.right)
            else:
                res.append(ans)
                ans=[] 
                q,q1 = q1,q
        return res   

    def levelOrder1(self, root: TreeNode):
        # 递归 recursion
        s = []
        if root == None:
            return s
        s.append(root)
        res = []
        self.levelOrderDFS(s,res)
        return res

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
            
            
            
        