class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertEnd(self, data):
        node = Node(data)
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def insertStart(self, data):
        node = Node(data)
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def delete(self, data):

        if self.head == None:
            print('Empty List')
            return

        # Last Node Deletion
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        # First Node Deletion
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        # Middle Node Deletion
        current = self.head
        while current:
            if current.data == data:
                break
            current = current.next
        if current == None:
            print('"' + str(data) + '" value does not exist in the list')
            return
        current.next.prev = current.prev
        current.prev.next = current.next

    def insertAfterPosition(self, data, position):
        if position<1:
            print('provide proper position.')
            return
        node = Node(data)
        if self.head == None and position == 0:
            self.head = node
            self.tail = node
            return
        curr = self.head
        for i in range(1, position):
            if curr.next:
                curr = curr.next
            else:
                print('position not available in LL')
                return
        print(curr.data, "--")

        node.prev = curr
        node.next = curr.next 
        curr.next = node
        if curr.next:
            curr.next.prev = node


        

    def printlist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    dll = DLinkedList()
    dll.insertEnd(1)
    dll.insertEnd(2)
    dll.insertEnd(3)
    dll.insertEnd(4)
    # dll.delete(1)
    # dll.delete(4)
    # dll.delete(5)
    # dll.printlist()
    dll.insertAfterPosition(data=5, position=2)
    dll.printlist()

