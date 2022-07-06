class Solution {
    func decompressRLElist(_ nums: [Int]) -> [Int] {
        
        var resArr:[Int] = []
        
        for i in stride(from: 0, to: nums.count-1, by: 2){
            let freq = nums[i]
            let val = nums[i+1]
            for _ in 1...freq{
                resArr.append(val)
            }
        }
        return resArr
    }
}