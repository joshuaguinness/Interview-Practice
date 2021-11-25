# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # Using List Comprehension
        
        if not root: 
            return []
        if root.right == None and root.left == None:
            return [str(root.val)]
        result = [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)]
        result += [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        return result