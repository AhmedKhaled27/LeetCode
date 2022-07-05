class Solution {
    func finalValueAfterOperations(_ operations: [String]) -> Int {
        var num = 0
        for operation in operations {
            switch operation{
            case "X++" , "++X":
                num+=1
            case "X--","--X":
                num-=1
            default:
                return 0
            }
        }
        
        return num
    }
}