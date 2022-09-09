class binary_treee:
    def __init__(self,data) -> None:
        self.data=data
        self.left_child=None
        self.right_child=None

New_tree=binary_treee(20)
leftChild=binary_treee('left1')
rightChild=binary_treee('right1')
New_tree.left_child=leftChild
New_tree.right_child=rightChild

#--.function to traverse the \tree according to Preorder

def Preorder()