class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        parenthessList = []
        result = ""
        
        for par in s :
            
            if par == "(" :
                if parenthessList :
                    result += par
                parenthessList.append(par)
            else :
                parenthessList.pop()
                if parenthessList :
                    result += par
                

        return result
            
            
        