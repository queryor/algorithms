# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# Example 1:

# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:

# Input: 1->1->1->2->3
# Output: 2->3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        newnode = ListNode(-1)
        pre = newnode
        newnode.next =head
        while(pre.next):
            cur = pre.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if cur !=pre.next:
                pre.next = cur.next
            else: 
                pre  = pre.next
        return newnode.next


# s= Solution()
# nums= [1,2,3,3,4,4,5]
# head = ListNode(nums[0])
# pre = head
# for i in range(1,len(nums)):
#      pre.next = ListNode(ListNode(nums[i]))
#      pre = pre.next
