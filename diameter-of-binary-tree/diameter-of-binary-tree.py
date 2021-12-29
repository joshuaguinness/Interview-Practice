# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0
        
        def dfs(node):
            # Non local variable declaration
            nonlocal diameter
            
            # Node is None
            if node == None:
                return 0
            
            # Lengths of left and right paths
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If sum of path lengths is more than current diameter
            # than a new longest path is found
            diameter = max(diameter, left + right)
            
            # Return longest of left and right, plus 1 for the
            # connection between node and parent
            return 1 + max(left, right)
            
        dfs(root)
        return diameter
        
        
            