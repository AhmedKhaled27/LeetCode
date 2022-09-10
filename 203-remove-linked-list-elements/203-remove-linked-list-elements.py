# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        newHead = head

        while newHead :
            if newHead.val == val :
                newHead = newHead.next
            else :
                break
        
        if not newHead :
            return newHead

        pre, curr = newHead, newHead.next

        while curr :
            if curr.val == val :
                pre.next = curr.next
                curr = curr.next
            else :
                pre = pre.next
                curr = curr.next
                

        return newHead
        