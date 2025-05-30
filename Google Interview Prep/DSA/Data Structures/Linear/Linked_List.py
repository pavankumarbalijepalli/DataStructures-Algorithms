class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
     
    
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, location: int = 0):
        node = Node(value)
        
        if not self.head:
            self.head = node
            self.tail = node
            return
        
        if location == 0:
            node.next = self.head
            self.head = node
            
        elif location == -1:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
            self.tail = node
            
            # SINCE WE HAVE TAIL - This works as well
            # self.tail.next = node
            # self.tail = node
            
        else:
            count = 0
            curr = self.head
            while curr.next:
                if count == location:
                    break
                curr = curr.next
                count += 1
            node.next = curr.next
            curr.next = node
            if not node.next:
                self.tail = node
        
    def traverse(self):
        if not self.head:
            return
        
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
        
sll = SLinkedList()
sll.insert(1, -1)
sll.insert(2, -1)
sll.insert(3, -1)
sll.insert(4, -1)
sll.insert(0, 0)
sll.insert(5, -1)
sll.insert(6, 2)

print([node.value for node in sll])
sll.traverse()