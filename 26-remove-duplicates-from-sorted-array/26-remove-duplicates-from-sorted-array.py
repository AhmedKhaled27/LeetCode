class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        number = nums[0]
        deletedNumbersCount = 0

        for i in range(len(nums)):
            if i == 0 :
                continue
            else:
                if nums[i-deletedNumbersCount] == number :
                    nums.pop(i-deletedNumbersCount)
                    deletedNumbersCount += 1
                else:
                    number = nums[i-deletedNumbersCount]    
  
        return len(nums)