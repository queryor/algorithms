# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

### 用一个数组把k个指针存下来，然后翻转

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        store = []
        cur = head
        for i in range(k):
            if cur==None:
                return head
            store.append(cur)
            cur = cur.next
        head = store[-1]
        p = head
        for j in range(k-1,-1,-1):
            p.next = store[j]
            p = p.next
        p.next = self.reverseKGroup(cur,k)
        return head