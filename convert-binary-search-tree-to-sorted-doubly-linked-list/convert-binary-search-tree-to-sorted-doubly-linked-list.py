"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        first = None
        last = None
               
        # In Order Transversal
        def transversalHelper(node):
            
            nonlocal last, first
            
            if node != None:
                
                # Transverse Left
                transversalHelper(node.left)
                
                # Current Node
                if last != None:
                    # Link the last node visited (previous)
                    # with the current node
                    last.right = node
                    node.left = last
                # Last does not exist, aka this is the first node
                # This will be rememberd
                else:
                    first = node
                # Remember the last node visited
                last = node
                
                # Transverse Right
                transversalHelper(node.right)
                
            return
            
        if not root:
            return None
        
        # In order transversal
        transversalHelper(root)
        
        # Close the circular loop
        first.left = last
        last.right = first
        
        return first