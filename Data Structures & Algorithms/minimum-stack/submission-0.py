class MinStack:

    def __init__(self):
        self.arr = []
        self.mini_arr = []
        self.idx = -1

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.idx == -1:
            self.mini_arr.append(val)
        else:
            self.mini_arr.append(min(val, self.mini_arr[self.idx]))
        self.idx += 1

    def pop(self) -> None:
        del self.arr[self.idx:]
        del self.mini_arr[self.idx:]
        self.idx -= 1

    def top(self) -> int:
        return self.arr[self.idx]

    def getMin(self) -> int:
        return self.mini_arr[self.idx]