# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iterative solution
        
        # Initialize
        head = current = ListNode(0)
        
        # Iterate through both nodes
        while list1 and list2:
            # Add to new LL from either list1
            # or list2 depending on which is smaller
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Advance current pointer
            current = current.next
            
        # Add the final node and return
        current.next = list1 or list2
        return head.next
                