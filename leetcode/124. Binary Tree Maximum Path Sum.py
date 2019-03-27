# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # DFS
        # https://www.hrwhisper.me/leetcode-tree/#124_Binary_Tree_Maximum_Path_Sum
        # 思路：DFS,设dfs(root)返回的是包括root这个结点的单一路径上的最大值。设L=dfs(root.left) ,R=dfs(root.right)如题目样例中的{1,2,3,}就是L=2,R=3

        # 则可能的结果有：

        #     1.L+R+root.val (左右子树和根构成路径为最大值，就是题目的情况）
        #     2.max(L,R) + root.val(左或者右子树和根构成最大值）
        #     3.root.val本身为最大值
        # 和全局变量ans比较更新即可。

        # 需要注意的是dfs返回值，可能是

        #     max(L,R) + root.val 某一条路径
        #     root.val  只是该结点（下面都是负的了）
        if root==None:
            return 0
        self.INF,self.ans=-0x7ffffff,-0x7ffffff   
        self.dfs(root)
        return self.ans
    def dfs(self,root:TreeNode):
        if not root:return self.INF
        L,R = self.dfs(root.left),self.dfs(root.right)
        if L+R+root.val>self.ans:self.ans = L+R+root.val
        if max(L,R)+root.val>self.ans:self.ans = max(L,R)+root.val
        if root.val>self.ans:self.ans = root.val
        return max(max(L,R)+root.val,root.val)
            

