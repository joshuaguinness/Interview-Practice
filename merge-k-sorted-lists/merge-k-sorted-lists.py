# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Brute force solution
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        new_list = sorted(nodes)
        for value in new_list:
            point.next = ListNode(value)
            point = point.next
            
        return head.next
        
        # Compare one by one solution
#         if not lists:
#             return None
        
#         head = point = ListNode(0)
        
#         # While there are still values in the list
#         while lists:
            
#             # Empty array
#             first_elements = []
            
#             # Iterate through the linked lists
#             for i, v in enumerate(lists):
                
#                 # If there is a linked List, add it to the array
#                 if v != None:
#                     first_elements.append((i, v))

#             # If there are no elements in the array, pop the last value in the list
#             if not first_elements:
#                 lists.pop()
            
#             else: 
#                 # Get the minimum value out of all LinkededLists
#                 min_small = min(first_elements,key=lambda x:x[1].val)
#                 # Add it to the new linked list
#                 point.next = ListNode(min_small[1].val)
#                 point = point.next
                
#                 # Pop the list itself is its empty
#                 if (min_small[1].next == None):
#                     lists.pop(min_small[0])
                    
#                 # Point to next value
#                 else:
#                     lists[min_small[0]] = min_small[1].next
#         return head.next
        