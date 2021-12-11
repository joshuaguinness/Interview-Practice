# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
               
        node_array = []
        
        # Iterate through the tree and add all node values to an array
        def inOrderDFS(node):
            
            if (node.left != None):
                inOrderDFS(node.left)
            node_array.append(node.val)
            if (node.right != None):
                inOrderDFS(node.right)
                
        # Construct the tree recursively
        def constructTree(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
                       
            node = TreeNode(node_array[mid])
            node.left = constructTree(left, mid-1)
            node.right = constructTree(mid+1, right)
            return node
            
            
        inOrderDFS(root)
        
        # Sort the array
        node_array.sort()
        
        return constructTree(0, len(node_array)-1)