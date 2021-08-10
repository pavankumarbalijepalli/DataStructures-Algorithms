# leftChild = Array[2 * parentNodeIndex]
# rightChild = Array[2 * parentNodeIndex + 1]

class Heap:
    def __init__(self, size):
        self.customList = [None] * (size+1)
        self.heapSize = 0
        self.maxSize = size+1


def peek(rootNode):
    if not rootNode:
        return rootNode
    else:
        return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return rootNode
    else:
        return rootNode.heapSize


def levelOrderTraversal(rootNode: Heap):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print('-'*((i)//2) + str(rootNode.customList[i]))


def heapifyTreeInsert(rootNode: Heap, index: int, heapType: str):
    parentIndex = index//2
    if index <= 1:
        return
    if heapType == 'Min':
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            (rootNode.customList[index],
             rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
                                                  rootNode.customList[index])
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == 'Max':
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            (rootNode.customList[index],
             rootNode.customList[parentIndex]) = (rootNode.customList[parentIndex],
                                                  rootNode.customList[index])
        heapifyTreeInsert(rootNode, parentIndex, heapType)


def insert(rootNode: Heap, nodeValue: int, heapType: str):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = int(nodeValue)
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Successfully inserted!"


def heapifyTreeExtract(rootNode: Heap, index: int, heapType: str):
    leftChild = index * 2
    rightChild = index * 2 + 1
    swapChild = 0

    # Check if rootNode has children
    if rootNode.heapSize < leftChild:
        return

    # If rootNode has only Left Child
    elif rootNode.heapSize == leftChild:
        if heapType == 'Min':
            if rootNode.customList[index] > rootNode.customList[leftChild]:
                (rootNode.customList[index],
                 rootNode.customList[leftChild]) = (rootNode.customList[leftChild],
                                                    rootNode.customList[index])
            return
        elif heapType == 'Max':
            if rootNode.customList[index] < rootNode.customList[leftChild]:
                (rootNode.customList[index],
                 rootNode.customList[leftChild]) = (rootNode.customList[leftChild],
                                                    rootNode.customList[index])
            return

    # If rootNode has both Children
    else:
        if heapType == 'Min':
            if rootNode.customList[leftChild] < rootNode.customList[rightChild]:
                swapChild = leftChild
            else:
                swapChild = rightChild

            if rootNode.customList[index] > rootNode.customList[swapChild]:
                (rootNode.customList[index],
                 rootNode.customList[swapChild]) = (rootNode.customList[swapChild],
                                                    rootNode.customList[index])
        elif heapType == 'Max':
            if rootNode.customList[leftChild] < rootNode.customList[rightChild]:
                swapChild = rightChild
            else:
                swapChild = leftChild
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                (rootNode.customList[index],
                 rootNode.customList[swapChild]) = (rootNode.customList[swapChild],
                                                    rootNode.customList[index])
        heapifyTreeExtract(rootNode, swapChild, heapType)


def extract(rootNode: Heap, heapType: str):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        (rootNode.customList[1],
         rootNode.customList[rootNode.heapSize]) = (rootNode.customList[rootNode.heapSize],
                                                    None)
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode


if __name__ == "__main__":
    customHeap = Heap(10)
    insert(customHeap, 1, 'Max')
    insert(customHeap, 2, 'Max')
    insert(customHeap, 3, 'Max')
    insert(customHeap, 4, 'Max')
    insert(customHeap, 5, 'Max')
    insert(customHeap, 6, 'Max')
    insert(customHeap, 7, 'Max')
    insert(customHeap, 8, 'Max')
    insert(customHeap, 9, 'Max')
    levelOrderTraversal(customHeap)
    print('----')
    extract(customHeap, 'Max')
    levelOrderTraversal(customHeap)
