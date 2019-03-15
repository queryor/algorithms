# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 先找到m,n 然后依次交换 
        # 应该可以边寻找边交换进行优化 依次插入到合适位置
        # Runtime: 48 ms, faster than 20.20% of Python3 online submissions for Reverse Linked List II.
        # Memory Usage: 13.1 MB, less than 5.22% of Python3 online submissions for Reverse Linked List II. 
        if n==m:
            return head
        newnode = ListNode(-1)
        newnode.next = head
        cur = newnode
        i=0
        ## 得到要交换的m上一个node n的node
        while cur!=None:
            if i==m-1:
                first_pre = cur
            elif i==n:
                second = cur
            i+=1
            cur=cur.next
        cur = first_pre.next
        last = second.next
        while cur!=second:
            t = cur.next
            cur.next = last
            last = cur
            cur = t
        return newnode.next
    def reverseBetween1(self, head: ListNode, m: int, n: int) -> ListNode:
        ## 未完成
        if n==m:
            return head
        newnode = ListNode(-1)
        newnode.next = head
        pre = newnode
        cur = newnode.next
        i = 1
        while cur.next !=None:
            pass
        