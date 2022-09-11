class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        0 1 0 3 12
        |
        1 0 0 3 12
          |  
        1 3 0 0 12
            |
        1 3 12 0 0
        
        """
        x = None
        for i in range(len(nums)) :
            if nums[i] == 0 :
                if not x :
                    x = i + 1
                for j in range(x,len(nums)):
                    if nums[j] != 0 :
                        nums[i], nums[j] = nums[j], nums[i]
                        x = j + 1
                        break
            else:
                continue