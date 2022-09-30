class MinStack:

    def __init__(self):
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack :
            lastMinValue = self.minStack[-1][1]
            minValue = min(val,lastMinValue)
            self.minStack.append((val,minValue))
        else :
            self.minStack.append((val,val))
            
    def pop(self) -> None:
        if self.minStack :
            self.minStack.pop()
        

    def top(self) -> int:
        if self.minStack :
            return self.minStack[-1][0]
        

    def getMin(self) -> int:
        if self.minStack :
            return self.minStack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()