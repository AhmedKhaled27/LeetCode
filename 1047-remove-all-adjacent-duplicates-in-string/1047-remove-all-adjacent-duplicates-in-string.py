class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        duplicateList = []
        for char in s :
            if not duplicateList :
                duplicateList.append(char)
            else :
                if char == duplicateList[-1] :
                    duplicateList.pop()
                else :
                    duplicateList.append(char)
            
        return ''.join(duplicateList)
            