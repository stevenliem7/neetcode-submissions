
class MinStack:

    def __init__(self):
        self.stk = []
        self.smallest = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.smallest) == 0:
            self.smallest.append(val)
            return None
        elif val > self.smallest[-1]:
            self.smallest.append(val)
            self.smallest.append(self.smallest[-2])
            return None
        else:
            self.smallest.append(self.smallest[-1])
            self.smallest.append(val)
            return None
        return None

    def pop(self) -> None:
        self.stk.pop()
        #print(str(self.smallest))
        if len(self.smallest) == 1:
            self.smallest.pop()
        else:
            self.smallest.pop()
            self.smallest.pop()
        return None

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.smallest[-1]

        
