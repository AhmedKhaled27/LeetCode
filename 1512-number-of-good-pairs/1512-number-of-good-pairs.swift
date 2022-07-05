class Solution {
    func numIdenticalPairs(_ nums: [Int]) -> Int {
        var pairsNum = 0
        for i in 0...nums.count-1{
            for j in 0...nums.count-1{
                if((nums[i] == nums[j]) && (i != j)){
                    pairsNum+=1
                }
            }
        }
        return pairsNum/2
    }
}