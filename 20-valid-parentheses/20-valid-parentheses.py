class Solution:
    def isValid(self, s: str) -> bool:
        
        validDic = {"]":"[",
                    "}":"{",
                    ")":"("}
        
        validList = []
        
        for char in s :
            if char == "(" or char == "[" or char == "{" :
                validList.append(char)
            else :
                if not validList :
                    return False
                
                elif validDic[char] == validList[-1] :
                    validList.pop()
                    
                else :
                    return False
        
        return True if len(validList) == 0 else False
                    
        