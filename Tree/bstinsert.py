class BST:
    def __init__(self,value) -> None:
        self.data=value
        self.left=None
        self.right=None
    def insert(self,value):
        if value ==self.data:
            return self
        if self.data==None:
            return BST(value)
        if value<self.data:
            if self.left==None:
                self.left=BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right==None:
                self.right=BST(value)
            else:
                self.right.insert(value)
    def preOrderTraversal(rootNode):
        if not rootNode:
            return
        print(rootNode.value)
        rootNode.left.preOrderTraversal()
        rootNode.right.preOrderTraversal()
        # preOrderTraversal(rootNode.left)
        # preOrderTraversal(rootNode.right)
# de f insertNode(rootNode, nodeValue):

n=BST(None)
n.insert(90)