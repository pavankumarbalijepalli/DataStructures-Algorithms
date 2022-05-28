from DS_Queue import Queue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printInLevels(rootNode, level=0, side='M'):
    if rootNode is None:
        # print('Tree does not exist')
        return
    else:
        print('  '*level + side + '|_' + str(rootNode.value))
        printInLevels(rootNode.left, level+1, side='L')
        printInLevels(rootNode.right, level+1, side='R')


def insertNode(rootNode, value):
    node = TreeNode(value)
    if rootNode is None:
        rootNode = node
    else:
        if value < rootNode.value:
            if rootNode.left is not None:
                insertNode(rootNode.left, value)
            else:
                rootNode.left = node
                return

        if value > rootNode.value:
            if rootNode.right is not None:
                insertNode(rootNode.right, value)
            else:
                rootNode.right = node
                return


def searchNode(rootNode, value):

    if rootNode.value == value:
        return 'Found'

    elif value < rootNode.value:
        if rootNode.left is not None:
            if rootNode.left.value == value:
                return 'Found'
            else:
                searchNode(rootNode.left, value)

    else:
        if rootNode.right is not None:
            if rootNode.right.value == value:
                return 'Found'
            else:
                searchNode(rootNode.right, value)


def minValueNode(rootNode):
    current = rootNode
    while (current.left is not None):
        current = current.left
    return current


def deleteNode(rootNode, value):
    if rootNode is None:
        return rootNode

    if value < rootNode.value:
        if rootNode.left is not None:
            rootNode.left = deleteNode(rootNode.left, value)

    elif value > rootNode.value:
        if rootNode.right is not None:
            rootNode.right = deleteNode(rootNode.right, value)

    else:
        if rootNode.left is None:
            temp = rootNode.right
            rootNode = None
            return temp

        if rootNode.right is None:
            temp = rootNode.left
            rootNode = None
            return temp

        temp = minValueNode(rootNode.right)
        rootNode.value = temp.value
        rootNode.right = deleteNode(rootNode.right, temp.value)

    return rootNode


def deleteBinaryTree(rootNode):
    rootNode.value = None
    rootNode.left = None
    rootNode.right = None


if __name__ == '__main__':
    bst = TreeNode(7)

    insertNode(bst, 5)
    insertNode(bst, 9)
    insertNode(bst, 3)
    insertNode(bst, 6)
    insertNode(bst, 8)
    insertNode(bst, 10)
    insertNode(bst, 2)
    insertNode(bst, 4)
    # deleteNode(bst, 7)
    # deleteBinaryTree(bst)

    print('  ')
    # print(searchNode(bst, 17))
    printInLevels(bst)
