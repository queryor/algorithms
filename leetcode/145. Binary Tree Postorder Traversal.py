'''Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        if root ==None:
            return res
        cur = root
        stack = []
        while len(stack)!=0 or cur!=None:
            if(cur):
                stack.append(cur)
                res.insert(0,cur.val)
                cur=cur.right
            else:
                t = stack.pop(-1)
                cur = t.left

        return res
        