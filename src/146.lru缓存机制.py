#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start

class CacheNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._head = CacheNode(-1, -1)
        self._tail = CacheNode(-1, -1)
        self._count = 0

        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        
        node = self._cache[key]
        self.removeNode(node)
        self.addToHead(node)

        return self._cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.value = value
            self.removeNode(node)
            self.addToHead(node)
        else:
            node = CacheNode(key, value)
            self._cache[key] = node
            self.addToHead(node)
            self._count += 1
            if self._count > self._capacity:
                self._count -= 1
                node = self._tail.prev
                self.removeNode(node)
                self._cache.pop(node.key)
                del node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev  = node.prev
    
    def addToHead(self, node):
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node
        

# from collections import OrderedDict

# class LRUCache(OrderedDict):

#     def __init__(self, capacity: int):
#         self._capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1

#         self.move_to_end(key)
#         return self[key]


#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)

#         self[key] = value
#         if len(self) > self._capacity:
#             self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

