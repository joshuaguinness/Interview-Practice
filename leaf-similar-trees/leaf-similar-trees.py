# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # Make two arrays of leaf nodes, see if they are similar
        root1_leaves = generateLeafValueSequence(root1)
        root2_leaves = generateLeafValueSequence(root2)
        
        return root1_leaves == root2_leaves

# Function to generate a list of leaf values using inorder transversal of a binary tree
def generateLeafValueSequence(node):
    leaves = []
    if (node.left == None and node.right == None):
        return [node.val]
    if (node.left != None):
        leaves += generateLeafValueSequence(node.left)
    if (node.right != None):
        leaves += generateLeafValueSequence(node.right)
        
    return leaves