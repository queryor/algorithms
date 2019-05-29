'''Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        ##先续遍历
        res = []
        if root ==None:
            return res
        q = []
        q.append(root)
        while len(q)!=0:
            cur = q.pop(0)
            res.append(cur.val)
            if cur.right:
                q.insert(0,cur.right)
            if cur.left:
                q.insert(0,cur.left)
        return res

        