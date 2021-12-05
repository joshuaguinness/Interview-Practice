# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        # Transverse BST using DFS
        # If value of node is in the range, add it to total
        def dfs(node, low, high):

            if node.val in range(low, high + 1):
                self.total += node.val      
            if (node.left != None):
                dfs(node.left, low, high)
            if (node.right != None):
                dfs(node.right, low, high)
                
        self.total = 0
        dfs(root, low, high)
        return self.total
    
        # Transverse BST using BFS