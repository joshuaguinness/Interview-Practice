"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        parents = set()
        
        def parentBack1(node):
            parents.add(node.val)
            if node.parent:
                parentBack1(node.parent)
        
        def parentBack2(node):
            if node.val in parents:
                return node
            if node.parent:
                return parentBack2(node.parent)
            return
            
        parentBack1(p)
        return parentBack2(q)
    
# There are other simpler ways if I checked the discussion