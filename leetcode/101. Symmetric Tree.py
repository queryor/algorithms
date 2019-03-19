# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # recursively
        # left tree is same as right tree
        # Runtime: 44 ms, faster than 68.17% of Python3 online submissions for Symmetric Tree.
        # Memory Usage: 13.2 MB, less than 5.61% of Python3 online submissions for Symmetric Tree.
        if root == None:
            return True
        # elif root.left==None and root.right==None:
        #     return True
        # elif root.left==None or root.right==None:
        #     return False
        else: 
            return self.isSymmetricDFS(root.left,root.right)
    def isSymmetricDFS(self,root1,root2):
        if root1==None and root2==None:
            return True
        elif root1==None or root2==None:
            return False
        else:
            if root1.val!=root2.val:
                return False
            else:
                return self.isSymmetricDFS(root1.left,root2.right) and self.isSymmetricDFS(root1.right,root2.left)
    def isSymmetric1(self, root: TreeNode) -> bool:
        # iteratively
        if root == None:
            return True
        q1 = queue.Queue()
        q2 = queue.Queue()
        q1.put(root.left)
        q2.put(root.right)
        while q1.qsize()!=0 and q2.qsize()!=0:
            node1 = q1.get()
            node2 = q2.get()
            if node1==None and node2==None:
                continue
            elif node1==None or node2==None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                q1.put(node1.left)
                q1.put(node1.right)
                q2.put(node2.right)
                q2.put(node2.left)
        return True