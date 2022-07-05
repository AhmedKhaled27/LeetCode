class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        var resArr:[Int] = []
        for i in 0...nums.count-1{
            var smallestCount = 0
            for j in 0...nums.count-1{
                if((nums[j]<nums[i]) && (i != j)){
                    smallestCount += 1
                }
            }
            resArr.append(smallestCount)
        }
        return resArr
    }
}