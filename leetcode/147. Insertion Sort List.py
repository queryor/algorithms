'''Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        ## Runtime: 2480 ms, faster than 8.66% of Python3 online submissions for Insertion Sort List.
        ## Memory Usage: 15.1 MB, less than 26.04% of Python3 online submissions for Insertion Sort List.
        ## 效率不高
        res = ListNode(0)
        if not head:
            return res.next
        cur = head
        while cur:
            #insert to right position
            cur_temp = cur.next
            p = res
            while p!=None:
                if p.next == None:
                    p.next = cur
                    cur.next = None
                    break
                elif p.next.val >= cur.val:
                    t = p.next
                    p.next = cur
                    cur.next = t
                    break
                p = p.next
            cur = cur_temp
        return res.next
    
    def insertionSortList1(self, head):
        # 效率更高
        if not head or not head.next:return head
        p = ListNode(-1)
        p.next, head=head,p
        tail =  head.next
        while tail.next:
            cur =tail.next
            if tail.val <= cur.val :
                tail = tail.next
            else:
                p ,prep= head.next,head
                while p.val < cur.val:
                    prep,p=prep.next,p.next
                self.delNode(tail,cur)
                self.insertNode(prep,cur)
        return head.next
    #del p from list, pre is previous node
    def delNode(self,pre,p):
        pre.next=p.next

    #insert p from list, pre is previous node
    def insertNode(self,pre,p):
        p.next , pre.next = pre.next , p