class Solution {
    func shuffle(_ nums: [Int], _ n: Int) -> [Int] {
        var resArr:[Int] = []
        for i in 0...n-1{
            resArr.append(nums[i])
            resArr.append(nums[i+n])
        }
        return resArr
    }
}