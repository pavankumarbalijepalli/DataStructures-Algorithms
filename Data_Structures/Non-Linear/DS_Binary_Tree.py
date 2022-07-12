from queue import Queue

class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)


def printInLevels(rootNode, level=0):
    if not (rootNode and rootNode.value):
        print('Tree does not exist')
        return
    else:
        print('  '*level + '|_' + rootNode.value)
        printInLevels(rootNode.left, level+1)
        printInLevels(rootNode.right, level+1)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.value)
    inOrderTraversal(rootNode.right)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        tqueue = Queue()
        tqueue.put(rootNode)
        while not(tqueue.empty()):
            root = tqueue.get()
            print(root.data)
            if (root.left is not None):
                tqueue.put(root.left)
            if (root.right is not None):
                tqueue.put(root.right)


def searchBinaryTree(rootNode, value):
    if rootNode is None:
        return 'Binary Tree is Empty.'
    else:
        squeue = Queue()
        squeue.put(rootNode)
        while not(squeue.empty()):
            root = squeue.get()
            if root.data == value:
                return '\nFound.'
            if (root.left is not None):
                squeue.put(root.left)
            if (root.right is not None):
                squeue.put(root.right)
        return '\nNot Found.'


def insertNode(rootNode, value):
    node = TreeNode(value)
    if rootNode is None:
        rootNode = node
    else:
        iq = Queue()
        iq.put(rootNode)
        while not(iq.empty()):
            root = iq.get()

            if root.left is not None:
                iq.put(root.left)
            else:
                root.left = node
                return

            if root.right is not None:
                iq.put(root.right)
            else:
                root.right = node
                return


def deepestNode(rootNode):
    if rootNode is None:
        return 'Empty'
    else:
        dq = Queue()
        dq.put(rootNode)
        while not(dq.empty()):
            root = dq.get()
            if root.left is not None:
                dq.put(root.left)
            if root.right is not None:
                dq.put(root.right)
        return root.data


def deleteDeepNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        dq = Queue()
        dq.put(rootNode)
        while not(dq.empty()):
            root = dq.get()
            if root.data is deepestNode:
                root.data = None
                return
            if root.left is not None:
                if root.left is deepestNode:
                    root.left = None
                    return
                else:
                    dq.put(root.left)

            if root.right is not None:
                if root.right is deepestNode:
                    root.right = None
                    return
                else:
                    dq.put(root.right)


def deleteNode(rootNode, value):
    if not rootNode:
        return
    else:
        dq = Queue()
        dq.put(rootNode)
        while not(dq.empty()):
            root = dq.get()
            if root.data == value:
                dnode = deepestNode(rootNode)
                root.data = dnode.value
                deleteDeepNode(rootNode, dnode)
                return 'Success'
            if (root.left is not None):
                dq.put(root.left)

            if (root.right is not None):
                dq.put(root.right)
        return 'Fail to Delete'


def deleteEntireBinaryTree(rootNode):
    rootNode.value = None
    rootNode.left = None
    rootNode.right = None


A = TreeNode(5)
insertNode(A, 1)
insertNode(A, 3)
insertNode(A, 2)
insertNode(A, 7)
insertNode(A, 8)
insertNode(A, 6)
insertNode(A, 4)
inOrderTraversal(A)
# hot = TreeNode('hot')
# cold = TreeNode('cold')
# coffee = TreeNode('coffee')
# tea = TreeNode('tea')
# alc = TreeNode('alcoholic')
# nalc = TreeNode('non-alcoholic')
# drinks.left = hot
# drinks.right = cold
# hot.left = coffee
# hot.right = tea
# cold.left = alc
# cold.right = nalc

# insertNode(drinks, 'capuccino')
# insertNode(drinks, 'mocha')
# insertNode(drinks, 'black tea')
# insertNode(drinks, 'green tea')
# insertNode(drinks, 'beer')
# insertNode(drinks, 'whisky')
# insertNode(drinks, 'ice tea')
# insertNode(drinks, 'mojito')

# deleteNode(drinks, 'tea')
# deleteEntireBinaryTree(drinks)
# printInLevels(drinks)
# print(searchBinaryTree(drinks, 'tea'))
