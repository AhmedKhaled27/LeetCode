class Solution {
    func runningSum(_ nums: [Int]) -> [Int] {
        var arrSum:[Int] = []
        var sum = 0
        
        for num in nums{
            sum+=num
            arrSum.append(sum)
        }
        return arrSum
    }
}