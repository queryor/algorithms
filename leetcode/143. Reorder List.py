'''Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next==None:
            return
        s = []
        cur = head.next
        while cur:
            s.append(cur)
            cur = cur.next
        cur = head
        n = len(s)
        for i in range(n):
            if i%2==0:
                t = s.pop(-1)
            else: 
                t = s.pop(0)
            cur.next = t
            cur = cur.next
        cur.next = None
    def reorderList1(self,head):
        # 这道链表重排序问题可以拆分为以下三个小问题：

        # 1. 使用快慢指针来找到链表的中点，并将链表从中点处断开，形成两个独立的链表。

        # 2. 将第二个链翻转。

        # 3. 将第二个链表的元素间隔地插入第一个链表中。
        pass
