'''Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if  not head or not head.next :return head
        p , one,two=ListNode(0),head,head
        p.next=head
        while two and two.next:
            p = one
            one , two = one.next,two.next.next
        p.next=None       
        lhead=self.sortList(head)
        rhead=self.sortList(one)
        return self.merge(lhead,rhead)

    def merge(self,lhead,rhead):       
        head = ListNode(-1)
        p,prep=None,head
        while lhead and rhead:
            if lhead.val < rhead.val:
                p ,lhead= lhead,lhead.next
            else:
                p,rhead=rhead,rhead.next
            prep.next=p
            prep=prep.next
        
        while lhead:
            p , lhead= lhead,lhead.next
            prep.next=p
            prep=prep.next
        while rhead:
            p,rhead=rhead,rhead.next
            prep.next=p
            prep=prep.next

        return head.next