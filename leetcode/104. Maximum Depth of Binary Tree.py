# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursion 52ms
        if root == None:
            return 0
        else: 
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepth1(self, root: TreeNode) -> int:
        # iteratively 88ms
        if root == None:
            return 0
        q = queue.Queue()
        res = 0
        q.put(root)
        while q.qsize()!=0:
            res +=1
            n = q.qsize()
            for i in range(n):
                node = q.get()
                if node.left !=None:
                    q.put(node.left)
                if node.right!=None:
                    q.put(node.right)

        return res
