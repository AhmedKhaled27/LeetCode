class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        
        let setNums = Set(nums)
        if(nums.count == setNums.count){
            return false
        }else{
            return true
        }
        
    }
}