class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        out  = []
        def traverse(root):
            if not root:
                return
            for child in root.children:
                traverse(child)
            print(root.val)
            print(root.children)
            out.append(root.val)
        traverse(root)
        return out