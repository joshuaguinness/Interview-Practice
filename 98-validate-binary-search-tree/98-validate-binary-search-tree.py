# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def validateTree(node, low=-math.inf, high=math.inf):
            
            # If Empty, still valid
            if not node:
                return True
                
            # Outside of bounds, needs to be between low and high
            if node.val <= low or node.val >= high:
                return False
            
            # Check left and right subtrees
            return validateTree(node.left, low, node.val) and validateTree(node.right, node.val, high)
            
        return validateTree(root)