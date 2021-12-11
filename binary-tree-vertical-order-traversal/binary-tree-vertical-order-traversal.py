# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # BFS w/ Sorting
        # if root is None:
        #     return []
#         columnTable = defaultdict(list)
#         queue = deque([(root, 0)])
        
#         while queue:
#             node, col = queue.popleft()
            
#             if node:
#                 columnTable[col].append(node.val)
                
#                 queue.append((node.left, col-1))
#                 queue.append((node.right, col+1))
            
#         # newList = []
#         # for i in sorted(columnTable):
#         #     newList.append(columnTable[i])
#         # return newList
#         return [columnTable[x] for x in sorted(columnTable.keys())]

        # BFS w/o Sorting
        if root is None:
            return []
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])
        min_col = 0
        max_col = 0
        
        while queue:
            node, col = queue.popleft()
            
            if node:
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                columnTable[col].append(node.val)
                
                queue.append((node.left, col-1))
                queue.append((node.right, col+1))
         
        new_list = []
        for i in range(min_col, max_col+1):
            new_list.append(columnTable[i])
        return new_list