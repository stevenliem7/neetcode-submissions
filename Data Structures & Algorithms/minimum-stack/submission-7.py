
class MinStack:

    def __init__(self):
        self.stk = []
        self.smallest = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.smallest) == 0:
            self.smallest.append(val)
        else:
            self.smallest.append(min(self.smallest[-1], val))
        return None

    def pop(self) -> None:
        self.stk.pop()
        #print(str(self.smallest))
        self.smallest.pop()
        return None

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.smallest[-1]

        
