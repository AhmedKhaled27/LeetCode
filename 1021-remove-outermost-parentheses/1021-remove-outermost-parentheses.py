class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
#         parenthessList = []
#         result = ""
        
#         for par in s :
             
#             if par == "(" :
#                 if parenthessList :
#                     result += par
#                 parenthessList.append(par)
#             else :
#                 parenthessList.pop()
#                 if parenthessList :
#                     result += par
                

#         return result

        count = 0
        result = ""
        
        for par in s :
             
            if par == "(" :
                if not count == 0 :
                    result += par
                count += 1
            else :
                count -= 1
                if not count == 0 :
                    result += par
                

        return result
            
            
        