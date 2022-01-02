class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

# Strategy: Dictionary with Double-Linked List
# Dict is <key, value> where key are keys, and values
# are nodes in the Linked List
# Linked List of all the values
# Head.next = least recently used, Tail.prev = most recently used
class LRUCache:
    
    # Delete a node from the Linked List
    def _deleteLL(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
    # Adds a node to the end of Linked List
    def _addLL(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
    
    def __init__(self, capacity: int):
        # Initialize LRU cache with positive size capacity
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.my_dict = {}
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:

        # Return -1 if key does not exist
        if key not in self.my_dict:
            return -1
            
        # Key exists already
        node = self.my_dict[key]
        # Delete from LL, then add again
        # Need to do that because adding it
        # Adds it to the tail making it most
        # recently used
        self._deleteLL(node)
        self._addLL(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        # Update the value of the key if the key exists
        if key in self.my_dict:
            self._deleteLL(self.my_dict[key])
            node = Node(key, value)
            self._addLL(node)
            self.my_dict[key] = node
        else: 
            # Otherwise add key-value pair to the cache
            if len(self.my_dict) < self.capacity:
                node = Node(key, value)
                self._addLL(node)
                self.my_dict[key] = node
            # If number of keys exceeds capacity, evict
            # the least recently used key
            else:
                node_delete = self.head.next
                self._deleteLL(node_delete)
                del self.my_dict[node_delete.key]
                
                node = Node(key, value)
                self._addLL(node)
                self.my_dict[key] = node
            
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)