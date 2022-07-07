class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        
        var bestSum = nums[0]
        var sum = 0
        
        for num in nums{
            sum += num
            if(sum>bestSum){
                bestSum = sum
            }
            if sum < 0 {
                sum = 0
            }
        }
        
        return bestSum
    }
}