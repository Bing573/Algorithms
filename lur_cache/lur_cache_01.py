"""
 Algorithm
 
 LUR Cache
"""
import unittest
from collections import OrderedDict

class LurCache(OrderedDict):
    
    def __init__(self, capacity):
        self.capacity = capacity
        
    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]
    
    def put(self, key, val):
        if key in self:
            self.move_to_end(key)
        self[key] = val
        if len(self) > self.capacity:
            self.popitem(last=False)
    
    
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
