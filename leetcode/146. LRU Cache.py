'''Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

## 解法
'''
构造函数中创建一个list q和一个字典dic
get时候，如果元素存在，将q中对应的key删除，并将其插入队尾
set时候，如果元素不存在且容量过大，删除队首元素，将新插入队尾和字典。如果元素存在，只需要设置字典，和将q中对应的调到队尾即可。（先删除后插入）
'''


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None
 
 
class DoubleLinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None
 
    def pop(self, node=None):
        if not node:
            node = self.tail
        pre, next = node.pre, node.next
        if pre and next:
            pre.next = next
            next.pre = pre
        
        if node == self.tail:
            self.tail = self.tail.pre
        if node == self.head:
            self.head = self.head.next
        return node
 
    def insert_head(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            node.pre = self.tail
            self.head.pre = node
            self.tail.next = node
            self.head = node
 
 
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}
        self.linklist = DoubleLinkList()
 
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key)
        if not node: return -1
        self.linklist.pop(node)
        self.linklist.insert_head(node)
        return node.value
 
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            node = self.linklist.pop(self.map[key])
            node.value = value
        else:
            if len(self.map) == self.capacity:
                node = self.linklist.pop()
                del self.map[node.key]
            node = Node(key, value)
            self.map[key] = node
        self.linklist.insert_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)