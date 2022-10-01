class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        numbersList = []
        
        for token in tokens :
            match token :
                case "+":
                    number1 = numbersList.pop()
                    number2 = numbersList.pop()
                    result = int(number2) + int(number1)
                    numbersList.append(result)
                
                case "-":
                    number1 = numbersList.pop()
                    number2 = numbersList.pop()
                    result = int(number2) - int(number1)
                    numbersList.append(result)
                    
                case "*":
                    number1 = numbersList.pop()
                    number2 = numbersList.pop()
                    result = int(number2) * int(number1)
                    numbersList.append(result)
                    
                case "/":
                    number1 = numbersList.pop()
                    number2 = numbersList.pop()
                    result = int(number2) / int(number1)
                    numbersList.append(int(result))
                    
                case default:
                    numbersList.append(token)

        
        return numbersList.pop()
            