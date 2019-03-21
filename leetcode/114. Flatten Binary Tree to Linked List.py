# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #http://www.cnblogs.com/grandyang/p/4293853.html
        # 思路是先利用DFS的思路找到最左子节点，然后回到其父节点，
        # 把其父节点和右子节点断开，将原左子结点连上父节点的右子节点上，
        # 然后再把原右子节点连到新右子节点的右子节点上，
        # 然后再回到上一父节点做相同操作。
        if root == None:
            return
        if root.left!=None:
            self.flatten(root.left)
        if root.right!=None:
            self.flatten(root.right)
        temp = root.right
        root.right = root.left
        root.left = None
        while(root.right!=None):
            root = root.right
        root.right = temp
    
    def flatten1(self,root)->None:
        # 非递归
        cur = root
        while(cur!=None):
            if cur.left:
                p = cur.left
                while(p.right):
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right