class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack():

    def __init__(self):
        self.base = None
        self.top = None
        self.size = 0

    def peek(self):
        if not self.base:
            print('Empty list')
        else:
            print(self.top.data)

    def push(self, value):
        node = Node(value)
        self.size += 1
        if self.base == None:
            self.base = node
            self.top = node
        else:
            self.top.next = node
            self.top = node

    def pop(self):
        if self.base == None:
            print('List is empty, cannot pop.')
        else:
            self.size -= 1
            current = self.base
            while (current.next).next:
                current = current.next
            temp = current.next
            current.next = None
            self.top = current
            print(str(temp.data) + ' is popped.')
            return temp.data

    def printstack(self):
        current = self.base
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        print(stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.printstack()
    stack.peek()
    print('size is')
    print(stack.size)
