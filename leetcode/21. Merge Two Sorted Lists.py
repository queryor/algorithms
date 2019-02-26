# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        pre = head
        while l1!=None and l2!=None:
            x1 = l1.val
            x2 = l2.val
            if x1<=x2:
                temp = ListNode(x1)
                l1 = l1.next
                if head == None:
                    head = temp
                    pre = head
                else: 
                    pre.next = temp
                    pre = pre.next
            else: 
                temp = ListNode(x2)
                l2=l2.next
                if head == None:
                    head = temp
                    pre = head
                else: 
                    pre.next = temp
                    pre = pre.next
        if l1 == None and l2 == None:
            return head
        elif l1 == None:
            if pre==None:
                head = l2
            else:
                pre.next = l2
        else:
            if pre==None:
                head = l1
            else: 
                pre.next = l1
        return head


a = ListNode(1)
b = None
s = Solution()
print(s.mergeTwoLists(a,b))


