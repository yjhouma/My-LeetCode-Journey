class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None
        # self.maximum = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum is None:
            self.minimum = val
        else:
            self.minimum = min(val, self.minimum)
        
        # if self.maximum is None:
        #     self.maximum = val
        # else:
        #     self.maximum = max(val, self.maximum)
        

    def pop(self) -> None:
        _ = self.stack.pop()
        if self.stack:
            self.minimum = min(self.stack)
        else:
            self.minimum = None

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()