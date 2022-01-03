# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        # List containing all last elements in level
        last = []
        
        # BFS 
        
        # Queue initialized with root element
        queue = deque([])
        queue.append(root)
        
        while queue:
            
            # Get the size of level based on
            # number of elements in the queue
            level_size = len(queue)
            
            # Iterate through all the elements in the level
            for i in range(level_size):
                
                node = queue.popleft()
                
                # Last element in the level
                if i == level_size-1:
                    last.append(node.val)
               
                # Add left and right elements, if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return last