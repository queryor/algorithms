# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example 1:

# Given the following tree [3,9,20,null,null,15,7]:

#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.

# Example 2:

# Given the following tree [1,2,2,3,3,null,null,4,4]:

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # recursion 84ms
        if root == None:
            return True
        elif abs(self.getDepth(root.left)-self.getDepth(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    def getDepth(self,root):
        if root ==None:
            return 0
        return 1 + max(self.getDepth(root.left),self.getDepth(root.right))

    def isBalanced1(self, root: TreeNode) -> bool:
        # 上面那个方法正确但不是很高效，因为每一个点都会被上面的点计算深度时访问一次，我们可以进行优化。
        # 方法是如果我们发现子树不平衡，则不计算具体的深度，而是直接返回-1。那么优化后的方法为：对于每一个节点，
        # 我们通过checkDepth方法递归获得左右子树的深度，如果子树是平衡的，则返回真实的深度，若不平衡，直接返回-1，
        # 此方法时间复杂度O(N)，空间复杂度O(H)
        # 60ms
        if self.checkDepth(root)==-1:
            return False
        return True
    def checkDepth(self,root:TreeNode):
        if root==None:
            return 0
        left = self.checkDepth(root.left)
        if left == -1:
            return -1
        right = self.checkDepth(root.right)
        if right == -1:
            return -1
        if abs(left-right)>1:
            return -1
        else: 
            return 1+max(left,right)
