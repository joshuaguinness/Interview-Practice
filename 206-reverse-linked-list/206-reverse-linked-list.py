# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Iterative
        # prev = None
        # curr = head
        # while curr != None:
        #     next_temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_temp
        # return prev
    
        # Recursive
        if (head == None) or (head.next == None):
            return head
        
        prev = self.reverseList(head.next)
        # Reverse part
        head.next.next = head
        # Pointing to None
        # If its the last element, then it will point
        # to None and be good
        head.next = None
        # This will be the new head/start of LL
        return prev