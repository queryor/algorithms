# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

 

# Example:



# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 

# Note:

# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.

#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# http://www.cnblogs.com/grandyang/p/4288151.html
import queue
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ## 层次遍历 recursion
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
        return root
    def connect1(self, root: 'Node') -> 'Node':
        # 非递归
        if not root:
            return
        q = []
        q.append(root)
        while len(q)!=0:
            size = len(q)
            for i in range(size):
                t = q.pop(0)
                if i<size-1:
                    t.next = q[0]
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        return root

    def connect2(self, root: 'Node') -> 'Node':
        # O(1)空间复杂度
        #用两个指针start和cur，其中start标记每一层的起始节点，cur用来遍历该层的节点，
        if not root:
            return root
        start = root
        cur = None
        while(start.left):
            cur = start
            while(cur):
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                    cur = cur.next
            start = start.left
        
        return root