

import numpy as np

class Node():
    def __init__(self, key=None, value=None ):
        self.key = key
        self.value = value
        self.before = None
        self.next = None 

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        
        self.start = Node('START', 'Start')
        self.end = Node('END', 'Start')
        
        self.start.next = self.end
        self.end.before = self.start
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        
        node = self.cache.get(key)
                
        if node is None: 
            print(-1)
            return -1 
        else:
            print(node.value)
            
            node.before.next = node.next
            node.next.before = node.before
            
            node.next = self.end
            node.before = self.end.before
            
            self.end.before = node
            self.end.before.next = node
            
            return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
           
                        
        if self.cache.get(key) == None:
            
            new_node = Node(key, value)
            
            new_node.before = self.end.before
            new_node.next = self.end
            
            self.end.before.next = new_node
            self.end.before = new_node
     
            self.cache[key] = new_node
            
            if len(self.cache) > self.capacity:
                
                LRU = self.start.next.key
                del self.cache[LRU]
                
                # delete the least recent used 
                object_to_delete = self.start.next 
                self.start.next = self.start.next.next
                self.start.next.next.before = self.start
                del object_to_delete
                

        
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
