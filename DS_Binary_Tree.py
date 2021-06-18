from DS_Queue import Queue


class TreeNode:
    def __init__(self, value):
        self.value = value
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
        tqueue.enque(rootNode)
        while not(tqueue.isEmpty()):
            root = tqueue.deque()
            print(root.data.value)
            if (root.data.left is not None):
                tqueue.enque(root.data.left)
            if (root.data.right is not None):
                tqueue.enque(root.data.right)


def searchBinaryTree(rootNode, value):
    if rootNode is None:
        return 'Binary Tree is Empty.'
    else:
        squeue = Queue()
        squeue.enque(rootNode)
        while not(squeue.isEmpty()):
            root = squeue.deque()
            if root.data.value == value:
                return '\nFound.'
            if (root.data.left is not None):
                squeue.enque(root.data.left)
            if (root.data.right is not None):
                squeue.enque(root.data.right)
        return '\nNot Found.'


def insertNode(rootNode, value):
    node = TreeNode(value)
    if rootNode is None:
        rootNode = node
    else:
        iq = Queue()
        iq.enque(rootNode)
        while not(iq.isEmpty()):
            root = iq.deque()

            if root.data.left is not None:
                iq.enque(root.data.left)
            else:
                root.data.left = node
                return

            if root.data.right is not None:
                iq.enque(root.data.right)
            else:
                root.data.right = node
                return


def deepestNode(rootNode):
    if rootNode is None:
        return 'Empty'
    else:
        dq = Queue()
        dq.enque(rootNode)
        while not(dq.isEmpty()):
            root = dq.deque()
            if root.data.left is not None:
                dq.enque(root.data.left)
            if root.data.right is not None:
                dq.enque(root.data.right)
        return root.data


def deleteDeepNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        dq = Queue()
        dq.enque(rootNode)
        while not(dq.isEmpty()):
            root = dq.deque()
            if root.data is deepestNode:
                root.data = None
                return
            if root.data.left is not None:
                if root.data.left is deepestNode:
                    root.data.left = None
                    return
                else:
                    dq.enque(root.data.left)

            if root.data.right is not None:
                if root.data.right is deepestNode:
                    root.data.right = None
                    return
                else:
                    dq.enque(root.data.right)


def deleteNode(rootNode, value):
    if not rootNode:
        return
    else:
        dq = Queue()
        dq.enque(rootNode)
        while not(dq.isEmpty()):
            root = dq.deque()
            if root.data.value == value:
                dnode = deepestNode(rootNode)
                root.data.value = dnode.value
                deleteDeepNode(rootNode, dnode)
                return 'Success'
            if (root.data.left is not None):
                dq.enque(root.data.left)

            if (root.data.right is not None):
                dq.enque(root.data.right)
        return 'Fail to Delete'


def deleteEntireBinaryTree(rootNode):
    rootNode.value = None
    rootNode.left = None
    rootNode.right = None


drinks = TreeNode('drinks')
hot = TreeNode('hot')
cold = TreeNode('cold')
coffee = TreeNode('coffee')
tea = TreeNode('tea')
alc = TreeNode('alcoholic')
nalc = TreeNode('non-alcoholic')
drinks.left = hot
drinks.right = cold
hot.left = coffee
hot.right = tea
cold.left = alc
cold.right = nalc

insertNode(drinks, 'capuccino')
insertNode(drinks, 'mocha')
insertNode(drinks, 'black tea')
insertNode(drinks, 'green tea')
insertNode(drinks, 'beer')
insertNode(drinks, 'whisky')
insertNode(drinks, 'ice tea')
insertNode(drinks, 'mojito')

# deleteNode(drinks, 'tea')
deleteEntireBinaryTree(drinks)
printInLevels(drinks)
# print(searchBinaryTree(drinks, 'tea'))
