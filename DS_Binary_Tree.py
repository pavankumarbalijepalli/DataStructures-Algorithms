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
                return 'Value Exists in the Binary Tree.'
            if (root.data.left is not None):
                squeue.enque(root.data.left)
            if (root.data.right is not None):
                squeue.enque(root.data.right)


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
levelOrderTraversal(drinks)
