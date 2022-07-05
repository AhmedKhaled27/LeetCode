class Solution {
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        
        guard let max = candies.max() else {return []}
        var resArr:[Bool] = []

        for candy in candies{
            let candyAfterExtra = candy + extraCandies
            if (candyAfterExtra >= max){
                resArr.append(true)
            }else{
                resArr.append(false)
            }
        }
        return resArr
    }
}