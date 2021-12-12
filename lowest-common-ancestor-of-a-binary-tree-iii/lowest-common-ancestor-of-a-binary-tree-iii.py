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
        
        parents = []
        
        def parentBack1(node):
            parents.append(node.val)
            if node.parent != None:
                parentBack1(node.parent)
        
        def parentBack2(node):
            if node.val in parents:
                return node
            if node.parent != None:
                return parentBack2(node.parent)
            return
            
        parentBack1(p)
        print(parents)
        lca = parentBack2(q)
        return lca