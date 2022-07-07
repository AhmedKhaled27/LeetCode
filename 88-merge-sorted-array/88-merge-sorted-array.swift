class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        
        if(m != 0){
            let resNums = nums1[0...m-1] + nums2
            nums1 = resNums.sorted(by: <)
        }else{
            let resNums = nums2
            nums1 = resNums.sorted(by: <)
        }
        
    }
}
