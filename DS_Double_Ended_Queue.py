class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DEQueue:
    def __init__(self):
        self.start = None
        self.end = None

    def enque_start(self, value):
        node = Node(value)
        if self.start == None:
            self.start = node
            self.end = node
        else:
            node.next = self.start
            self.start = node

    def enque_end(self, value):
        node = Node(value)
        if self.start == None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def deque_start(self):
        if self.start == None:
            print('Queue Empty')
        else:
            self.start = self.start.next

    def deque_end(self):
        if self.start == None:
            print('Queue Empty')
        else:
            current = self.start
            while current.next.next:
                current = current.next
            current.next = None
            self.end = current

    def printqueue(self):
        current = self.start
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    d = DEQueue()
    d.enque_start(1)
    d.enque_start(2)
    d.enque_start(3)
    d.enque_end(0)
    d.deque_end()
    d.printqueue()
