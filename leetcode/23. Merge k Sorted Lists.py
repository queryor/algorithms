# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

## http://www.cnblogs.com/grandyang/p/4606710.html

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if len(lists)==0:
            return None
        n = len(lists)g
        while(n>1):
            k = (n+1)//2
            for i in range(n//2):
                lists[i]=self.mergeTwoLists(lists[i],lists[i+k])
            n = k
        return lists[0]
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