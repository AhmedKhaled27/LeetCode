class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int] :
       
        numsLenght = len(nums)
        k = k % numsLenght
        

        l = 0
        r = numsLenght - 1
        self.reverseList(nums, l ,r)
        
        l = 0 
        r = k - 1
        self.reverseList(nums, l, r)

        l = k 
        r = numsLenght - 1
        self.reverseList(nums, l, r)


    def reverseList(self, nums:List[int], l:int, r:int):

        while l < r :
            nums[l] ,nums[r] = nums[r] ,nums[l]
            l += 1
            r -= 1

