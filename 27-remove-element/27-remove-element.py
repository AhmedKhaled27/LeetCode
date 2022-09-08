class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        deletedNumbersCount = 0

        for i in range(len(nums)):
            
            if nums[i-deletedNumbersCount] == val :
                nums.pop(i-deletedNumbersCount)
                deletedNumbersCount += 1

        return len(nums)