class Heap:
    def __init__(self, size):
        self.customList = [None] * (size+1)
        self.heapSize = 0
        self.maxSize = size+1


def heapifyInsert(rootNode: Heap, index: int):
    parentIndex = index//2
    if index <= 1:
        return
    if rootNode.customList[index] > rootNode.customList[parentIndex]:
        (rootNode.customList[index],
         rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
                                              rootNode.customList[index])
        heapifyInsert(rootNode, parentIndex)


def insert(rootNode: Heap, nodeValue: int):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return 'Heap Full'
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsert(rootNode, rootNode.heapSize)


if __name__ == '__main__':
    nh = Heap(5)
    insert(nh, 5)
    insert(nh, 1)
    insert(nh, 2)
    insert(nh, 3)
    insert(nh, 6)
    print(nh.customList)
