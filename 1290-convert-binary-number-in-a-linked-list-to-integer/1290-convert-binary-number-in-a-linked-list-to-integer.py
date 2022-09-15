# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        lenght = 0
        p = head 
        while p :
            lenght += 1
            p = p.next
            
        i = lenght-1
        number = 0 
        
        while head :
            number += head.val * (2**i)
            i -= 1
            head = head.next
            
        return number