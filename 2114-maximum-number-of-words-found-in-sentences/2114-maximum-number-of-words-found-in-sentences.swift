class Solution {
    func mostWordsFound(_ sentences: [String]) -> Int {
        var maxNumWords = 0
        
        for sentence in sentences{
            var numWords = 0
            for (i,char) in sentence.enumerated(){
                if ((char == " ") || (i == sentence.count-1)){
                    numWords+=1
                }
            }
            if numWords > maxNumWords{
                maxNumWords = numWords
            }
        }
        return maxNumWords
    }
}
