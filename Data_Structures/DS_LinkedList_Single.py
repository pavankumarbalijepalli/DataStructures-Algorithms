class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertFirst(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insertLast(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = None
            self.tail.next = node
            self.tail = node

    def insertAfter(self, value, node):
        current = self.head
        insertNode = Node(value)
        while current.value != node.value:
            current = current.next
        insertNode.next = current.next
        current.next = insertNode

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = self.head.next
            return
        while current:
            if current.next.value == value:
                break
            else:
                current = current.next
        current.next = current.next.next

    def search(self, node):
        if self.head == None:
            print('Empty Linked List.')
        else:
            current = self.head
            while current != None and current.value != node.value:
                current = current.next
            if current == None:
                print('Value not found!')
                return False
            else:
                print('Value Found')
                return True

    def printlist(self):
        last = self.head
        if last == None:
            print('Empty')
        while last != None:
            print(last.value)
            last = last.next


def main():
    print(' ')
    ll = LinkedList()
    ll.insertLast(4)
    ll.insertLast(3)
    ll.insertLast(5)
    ll.insertAfter(7, Node(5))
    ll.delete(7)
    ll.printlist()


if __name__ == "__main__":
    main()
