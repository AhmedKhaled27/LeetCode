# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        count = 0
        pHead = head
        while pHead :
            count += 1
            pHead = pHead.next
            
        if count == 0 :
            return head
        elif count == n :
            head = head.next
            return head
        
        prev = None 
        curr = head
        for i in range(1,count) :
            prev = curr 
            curr = curr.next
            if count - i == n :
                prev.next = curr.next
                return head
                
                
        