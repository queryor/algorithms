# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 1->1->2
# Output: 1->2
# Example 2:

# Input: 1->1->2->3->3
# Output: 1->2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next==None:
            return head
        pre = head
        cur = pre.next
        while cur!=None:
            ## 找到第一个不等于的pre.val的cur listnode 或者 空
            while cur!=None and cur.val==pre.val:
                cur=cur.next
            pre.next = cur
            pre = pre.next
            if cur == None:
                break
            cur = cur.next
        return head

