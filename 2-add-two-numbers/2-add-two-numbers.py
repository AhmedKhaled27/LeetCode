# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        newList = None
        newListHead = None
        reminder = 0
        
        while l1 and l2 :
            
            sum = l1.val + l2.val + reminder
            reminder = 0
            
            if sum == 10 :
                sum = 0
                reminder = 1
            elif sum > 10 :
                reminder = int(sum/10)
                sum = sum - 10
            
            if not newList :
                newList = ListNode(sum,None)
                newListHead = newList
            else :
                node = ListNode(sum,None)
                newList.next = node
                newList = newList.next
                
            l1 = l1.next
            l2 = l2.next
            
            
        while l1 :
            sum = l1.val + reminder
            reminder = 0

            if sum == 10 :
                sum = 0
                reminder = 1
            elif sum > 10 :
                reminder = int(sum/10)
                sum = sum - 10
            
            node = ListNode(sum,None)
            newList.next = node
            newList = newList.next
                
            l1 = l1.next
            
        while l2 :
            sum = l2.val + reminder
            reminder = 0

            if sum == 10 :
                sum = 0
                reminder = 1
            elif sum > 10 :
                reminder = int(sum/10)
                sum = sum - 10
            
            node = ListNode(sum,None)
            newList.next = node
            newList = newList.next
                
            l2 = l2.next
            
        if reminder != 0 :
            
            node = ListNode(reminder,None)
            newList.next = node
            newList = newList.next
        
        return newListHead
    
    
    def reverseList(self, list:[ListNode]) -> [ListNode]:
        
        curr = list 
        prev = None 
        
        while curr :
            next = curr.next 
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
            
            
        
        