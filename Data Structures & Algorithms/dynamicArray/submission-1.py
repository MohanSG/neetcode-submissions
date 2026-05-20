class DynamicArray:
    
    def __init__(self, capacity: int):
        self.list = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.list[i]

    def set(self, i: int, n: int) -> None:
        self.list[i] = n

    def pushback(self, n: int) -> None:
        if self.size == len(self.list):
            self.resize()

        self.list[self.size] = n
        self.size += 1

    def popback(self) -> int:
        lastElement = self.list[self.size - 1]
        self.list[self.size - 1] = None
        self.size -= 1
        return lastElement

    def resize(self) -> None:
        self.list.extend([None] * len(self.list))

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return len(self.list)