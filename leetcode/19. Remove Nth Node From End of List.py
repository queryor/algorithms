# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_val(self):
        print(self.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        p = head
        while p!=None:
            nodes.append(p)
            p = p.next
        if nodes==[]:
            return None
        if nodes[-n]==head:
            head = head.next
        else:    
            nodes[-n-1].next = nodes[-n].next
        return head
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None
        first = head
        seccond = head
        p  = head
        for i in range(n):
            seccond = seccond.next
        if seccond == None:
            head = head.next
        while seccond!=None:
            p = first
            first = first.next
            seccond = seccond.next
        p.next = first.next
        return head

s = Solution()
a = ListNode(1)
p = a 
# for i in range(2,6):
#     p.next = ListNode(i)
#     p = p.next
print(s.removeNthFromEnd1(a,1))