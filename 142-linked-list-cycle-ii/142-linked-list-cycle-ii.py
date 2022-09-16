# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         nodesSet = set()
#         while head :
#             if(head in nodesSet):
#                 return head 
#             else :
#                 nodesSet.add(head)
            
#             head = head.next
                
#         return None
    
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        fast = head 
        slow = head
        
        curr = None
        cycleLenght = 0
        
        while fast and fast.next :
            
            slow = slow.next 
            fast = fast.next.next
            
            if (fast == slow) :
                
                curr = slow
                slow = slow.next 
                cycleLenght = 1
                
                while curr != slow :
                    cycleLenght += 1
                    slow = slow.next
                    
                p1 = head 
                p2 = head 
                
                for i in range(cycleLenght) :
                    p1 = p1.next
                
                while p1 :
                    if p1 == p2 :
                        return p1 
                    
                    p1 = p1.next 
                    p2 = p2.next
        
        return None
                
    
            
        