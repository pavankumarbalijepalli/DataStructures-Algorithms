# Priority Queue
class Heap:
    def __init__(self, size):
        self.customList = [None] * (size+1)
        self.heapSize = 0
        self.maxSize = size+1

# Heapifying the rootNode.customList by checking the min_max rule.
def heapifyTreeInsert(rootNode: Heap, index: int, heapType: str):
    parentIndex = index//2
    if index<=1:
        return
    
    if heapType == "min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            (rootNode.customList[index],
            rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
                                                rootNode.customList[index])
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == "max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            (rootNode.customList[index],
            rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
                                                rootNode.customList[index])
        heapifyTreeInsert(rootNode, parentIndex, heapType)

# We insert the value at the end of the array and then heapify it.
def insert(rootNode: Heap, value: int, heapType: str):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Heap Full"
    rootNode.customList[rootNode.heapSize+1] = value
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)

# Heapifying rootNode.customList when value is removed from the list.
def heapifyTreeExtract(rootNode: Heap, index: int, heapType: str):
    leftChild = (index * 2)
    rightChild = (index * 2) + 1
    swapChild = 0

    # If RootNode has no children
    if rootNode.heapSize < leftChild:
        return

    # If Rootnode has only left child, we check which has more priority
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

    # If RootNode has both children, we get the swapchild and swap based on which is bigger
    if rootNode.heapSize > leftChild:
        if heapType == 'max':
            if rootNode.customList[leftChild] < rootNode.customList[rightChild]:
                swapChild = rightChild
            else:
                swapChild = leftChild
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                (rootNode.customList[index], 
                rootNode.customList[swapChild]) = (rootNode.customList[swapChild],
                rootNode.customList[index])
        
        if heapType == 'min':
            if rootNode.customList[leftChild] < rootNode.customList[rightChild]:
                swapChild = leftChild
            else:
                swapChild = rightChild
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                (rootNode.customList[index], 
                rootNode.customList[swapChild]) = (rootNode.customList[swapChild],
                rootNode.customList[index])
        heapifyTreeExtract(rootNode, swapChild, heapType)

# Removing the value from list and then heapifying the list.
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
    customHeap = Heap(10)
    insert(customHeap, 1, 'max')
    insert(customHeap, 2, 'max')
    insert(customHeap, 3, 'max')
    insert(customHeap, 4, 'max')
    insert(customHeap, 5, 'max')
    insert(customHeap, 6, 'max')
    insert(customHeap, 7, 'max')
    insert(customHeap, 8, 'max')
    insert(customHeap, 9, 'max')
    insert(customHeap, 0, 'max')

    # Print Heap
    print(customHeap.customList)

    # Extracting
    print(extract(customHeap, 'max'))
    print(customHeap.customList)
