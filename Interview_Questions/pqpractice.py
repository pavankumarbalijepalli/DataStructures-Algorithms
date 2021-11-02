class Heap:
    def __init__(self, size):
        self.customList = [None]* (size+1)
        self.heapSize = 0
        self.maxSize = size + 1

def heapifyTreeInsert(rootNode: Heap, index: int, heapType: str):
    parentIndex = index//2
    if index<=1:
        return rootNode

    if heapType == 'min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            (rootNode.customList[index], 
            rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
            rootNode.customList[index])
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    
    if heapType == 'max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            (rootNode.customList[index], 
            rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
            rootNode.customList[index])
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insert(rootNode: Heap, value: int, heapType: str):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return 'Heap is full.'
    rootNode.customList[rootNode.heapSize + 1] = value
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)

def heapifyTreeExtract(rootNode: Heap, index: int, heapType: str):
    leftChild = index * 2
    rightChild = index * 2 + 1
    swapChild = 0

    # if no children to rootnode
    if rootNode.heapSize < leftChild:
        return rootNode
    
    # if only left child
    if rootNode.heapSize == leftChild:
        if heapType == 'max':
            if rootNode.customList[index] < rootNode.customList[leftChild]:
                (rootNode.customList[index],
                rootNode.customList[leftChild]) = (rootNode.customList[leftChild],
                rootNode.customList[index])
        
        if heapType == 'min':
            if rootNode.customList[index] > rootNode.customList[leftChild]:
                (rootNode.customList[index],
                rootNode.customList[leftChild]) = (rootNode.customList[leftChild],
                rootNode.customList[index])

    # if both left and right child
    if rootNode.heapSize > leftChild:
        if heapType == 'min':
            if rootNode.customList[leftChild] < rootNode.customList[rightChild]:
                swapChild = leftChild
            else:
                swapChild = rightChild
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                (rootNode.customList[index], 
                rootNode.customList[swapChild]) = (rootNode.customList[swapChild],
                rootNode.customList[index])
        
        if heapType == 'max':
            if rootNode.customList[leftChild] > rootNode.customList[rightChild]:
                swapChild = leftChild
            else:
                swapChild = rightChild
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                (rootNode.customList[index], 
                rootNode.customList[swapChild]) = (rootNode.customList[swapChild],
                rootNode.customList[index])
        heapifyTreeExtract(rootNode, swapChild, heapType)

def extract(rootNode: Heap, heapType: str):
    if rootNode.heapSize == 0:
        return
    extractedNode = rootNode.customList[1]
    (rootNode.customList[1], 
    rootNode.customList[rootNode.heapSize]) = (rootNode.customList[rootNode.heapSize],
    None)
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode


if __name__ == "__main__":
    customHeap = Heap(5)
    insert(customHeap, 5, 'max')
    insert(customHeap, 6, 'max')
    insert(customHeap, 7, 'max')
    insert(customHeap, 8, 'max')
    insert(customHeap, 9, 'max')
    print(customHeap.customList)
    print(extract(customHeap, 'max'))
    print(extract(customHeap, 'max'))
    print(extract(customHeap, 'max'))
