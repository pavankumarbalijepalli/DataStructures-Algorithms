class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def isEmpty(self):
        return self.start == None

    def enque(self, value):
        node = Node(value)
        if self.start == None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def deque(self):
        if self.start == None:
            print('Queue empty.')
        else:
            temp = self.start
            self.start = self.start.next
            return temp

    def printqueue(self):
        current = self.start
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    q = Queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    q.enque(5)
    print(q.deque())
    q.deque()
    q.printqueue()
