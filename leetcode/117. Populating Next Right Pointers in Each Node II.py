
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
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