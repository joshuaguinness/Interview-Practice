# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        values = []
        self.recursiveFunction(root, values, 0)
        return values
    
    def recursiveFunction(self, node: Optional[TreeNode], values, level):
        
        if node is None:
            return
        
        if len(values) <= level:
            values.append([])
        values[level].append(node.val)
        self.recursiveFunction(node.left, values, level+1)
        self.recursiveFunction(node.right, values, level+1)