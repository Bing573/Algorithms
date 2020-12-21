"""
 Algorithm
 
 LUR Cache
"""

import unittest


class LurCache(object):
    
    def __init__(self, capacity):
        self.cache = dict()
        self.capacity = capacity
        self.head = Node() # dummy head
        self.tail = Node() # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_end(node)
            node.value = val
        else:
            node = Node(key, val)
            self.cache[key] = node
            self.append(node)
            if len(self.cache) > self.capacity:
                poped = self.pop_head()
                del self.cache[poped.key]
            
        
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_end(node)
        return node.value
        
    
    def append(self, node):
        tail_node = self.tail.prev
        tail_node.next = node
        node.prev = tail_node
        node.next = self.tail
        self.tail.prev = node
        
    def pop_head(self):
        head_node = self.head.next
        head_node.prev.next = self.head
        self.head.next = head_node.next
        return head_node
    
    def move_to_end(self, node):
        tail_node = self.tail.prev
        if tail_node.key == node.key:
            return
        tail_node.next = node
        node.prev = tail_node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev = node
        node.next = self.tail

        

class Node (object):
    
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None
            

class LurCacheTestCase(unittest.TestCase):
    
    def test(self):
        lur_cache = LurCache(2)
        lur_cache.put(1,1)
        lur_cache.put(2,2)
        self.assertEqual(1, lur_cache.get(1))
        self.assertEqual(2, lur_cache.get(2))
        
        lur_cache.put(3,3)
        self.assertEqual(-1, lur_cache.get(1))
        
        lur_cache.put(4, 4)
        self.assertEqual(-1, lur_cache.get(2))
        self.assertEqual(3, lur_cache.get(3))
        self.assertEqual(4, lur_cache.get(4))
        

if __name__ == '__main__':
    unittest.main()
    
