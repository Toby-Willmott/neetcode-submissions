class Node: 
    def __init__(self, key, val): 
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.start = Node(0,0)
        self.end = Node(0,0)

        self.start.next = self.end
        self.end.prev = self.start 
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next 

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.end.prev
        nxt = self.end

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else: 
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: 
            lru = self.start.next
            self.remove(lru)
            self.cache.pop(lru.key)
