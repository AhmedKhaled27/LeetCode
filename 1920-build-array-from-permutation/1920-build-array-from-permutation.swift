class Solution {
    func buildArray(_ nums: [Int]) -> [Int] {
        var ans:[Int] = []
        for (i,_num) in nums.enumerated(){
            ans.append(nums[nums[i]])
        }
        return ans
    }
}