# Question: https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        self.data = []
        
    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        temp = self.data[0]
        self.data = self.data[1:]
        return temp

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return self.data==[]