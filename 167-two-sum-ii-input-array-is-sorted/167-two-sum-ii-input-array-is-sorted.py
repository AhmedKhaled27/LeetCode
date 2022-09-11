class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        preNumber = numbers[0]
        
        for i in range(len(numbers)):
        
            if(i != 0 and numbers[i] == preNumber):
                continue
            else :
                preNumber = numbers[i]
                
            expectedNumber = target - numbers[i]
                
            for j in range(i+1,len(numbers)) :
                if numbers[j] == expectedNumber :
                    return [i+1,j+1]
                elif numbers[j] > target :
                    break
                    