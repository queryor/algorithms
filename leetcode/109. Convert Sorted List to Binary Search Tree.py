# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Example:

# Given the sorted linked list: [-10,-3,0,5,9],

# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 把链表转化成list 然后调用108题的函数
        nums = []
        p = head
        while p!=None:
            nums.append(p.val)
            p=p.next
        return self.sortedArrayToBST(nums)
    
    def sortedArrayToBST(self, nums) -> TreeNode:
        ## 直接递归 recursion
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        cur = TreeNode(nums[mid])
        cur.left = self.sortedArrayToBST(nums[:mid])
        cur.right = self.sortedArrayToBST(nums[mid+1:]) 
        return cur