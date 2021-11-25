# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # Using List Comprehension
        
        # if not root: 
        #     return []
        # if root.right == None and root.left == None:
        #     return [str(root.val)]
        # result = [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)]
        # result += [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        # return result
        
        
        # Recursive DFS
#         if not root:
#             return []
        
#         result = []
#         self.dfs(root, result, "")
#         return result
#     def dfs(self, root, result, string):
#         if root.left == None and root.right == None:
#             result.append(string + str(root.val))
#             return
#         if root.left != None:
#             self.dfs(root.left, result, string + str(root.val) + "->")
#         if root.right != None:
#             self.dfs(root.right, result, string + str(root.val) + "->")
        
        # BFS w/ Queue
        if not root:
            return []
        
        result = []
        queue =  collections.deque([(root, "")])
        while queue:
            node, string = queue.popleft()
            if node.left == None and node.right == None:
                result.append(string + str(node.val))
            if node.left:
                queue.append((node.left, string + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, string + str(node.val) + "->"))
        
        return result