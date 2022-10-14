class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        p1 = len(digits) - 1
        reminder = 0 
        
        while p1 >= 0 :
            newDigit = digits[p1] + 1
            if newDigit > 9 :
                digits[p1] = newDigit - 10
                reminder = 1
                p1 -= 1
                
            else :
                reminder = 0
                digits[p1] = newDigit 
                return digits
            
        if reminder != 0 :
            return [1] + digits
        
        
        """
        9999
        
        """
