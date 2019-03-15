# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Definition for a binary tree node.
# Follow up: Recursive solution is trivial, could you do it iteratively?
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        ## 递归
        ans = []
        def inorderDFS(root:TreeNode):
            if root==None:
                pass
            else: 
                inorderDFS(root.left)
                ans.append(root.val)
                inorderDFS(root.right)
        inorderDFS(root)
        return ans

    def inorderTraversal1(self,root:TreeNode):
        ## iteratively 使用stack
        stack = []
        ans = []
        p = root 
        while p!=None or len(stack)!=0:
            while p !=None:
                stack.append(p)
                p=p.left
            p = stack.pop()
            ans.append(p.val)
            p = p.right        
        return ans

    def inorderTraversal2(self,root:TreeNode):
        # Morris Traversal
        # http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
        res = []
        if root == None:
            return res
        cur = root
        while cur!=None:
            if cur.left == None:
                res.append(cur.val)
                cur=cur.right
            else: 
                pre = cur.left
                while pre.right!=None and pre.right!=cur:
                    pre=pre.right
                if pre.right == None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    res.append(cur.val)
                    cur = cur.right
        return res