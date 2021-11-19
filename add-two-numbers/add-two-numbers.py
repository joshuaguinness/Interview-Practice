# Definition for singly-linked list.
# class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1.val
        num2 = l2.val
        i = 1
        while (l1.next != None):
            l1 = l1.next
            num1 += l1.val * (10**i)
            i += 1
        j = 1
        while (l2.next != None):
            l2 = l2.next
            num2 += l2.val * (10**j)
            j += 1
        
        sum = num1 + num2
        x = [int(a) for a in str(sum)]
        output = None
        
        for digit in x:
            output = ListNode(digit, output)
            
        return output
        
        