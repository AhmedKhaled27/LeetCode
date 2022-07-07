class Solution {
    func restoreString(_ s: String, _ indices: [Int]) -> String {
        
        var charArr:[Character] = []
        for char in s{
            charArr.append(char)
        }
        
        for (i,char) in charArr.enumerated(){
            let newIndex = indices[i]
            charArr[newIndex] = char
        }
        
        return String(charArr)
        
    }
}