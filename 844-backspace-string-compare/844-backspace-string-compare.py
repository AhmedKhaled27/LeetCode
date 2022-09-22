class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sList = []
        tList = []
        
        for char in s :
            if char != "#" :
                sList.append(char)
            else :
                if sList:
                    sList.pop()
        
        for char in t :
            if char != "#" :
                tList.append(char)
            else:
                if tList:
                    tList.pop()
                
        return sList == tList