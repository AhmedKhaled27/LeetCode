# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodesSet = set()
        while head :
            if(head in nodesSet):
                return head 
            else :
                nodesSet.add(head)
            
            head = head.next
                
        return None
            
        