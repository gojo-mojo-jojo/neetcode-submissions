class MinStack:

    def __init__(self):
        self.d_array =  []
        

    def push(self, val: int) -> None:
        self.d_array.append(val)
        pass
        

    def pop(self) -> None:
        return self.d_array.pop()
        

    def top(self) -> int:
        return self.d_array[-1]

    def getMin(self) -> int:
        return min(self.d_array)
        
