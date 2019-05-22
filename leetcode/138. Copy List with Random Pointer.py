'''A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
'''


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ## 直接在原来基础上复制
        # copy 
        p = head
        while p!=None:
            t = Node(p.val,p.next,None)
            p.next = t
            p = t.next
        ## 修改random
        cur = head
        if head==None:
            new_head = None
        else:
            new_head = head.next
        while cur!=None:
            cur.next.random = cur.random.next if cur.random!=None else None
            cur = cur.next.next
        ## 拆分链表
        cur = head
        while cur!=None:
            t = cur.next.next
            if t!=None:
                cur.next.next = t.next
            cur.next = t
            cur = cur.next
        return new_head
h1 = Node(2,None,None)
head = Node(1,h1,h1)
s = Solution()
new_head =(s.copyRandomList(head))
p = new_head
while p:
    print(p.val,end=" ")
    p = p.next