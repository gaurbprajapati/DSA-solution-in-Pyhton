class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None
        
class Linkedlist:
    def __init__(self) -> None:
        self.head=None
        
    #this to traverse the linked list -->
    def printall(self):
        if self.head is None:
            print("The given linked list is empty.")
        else:
            n=self.head
            while(n is not None):
                print(n.data)
                n=n.ref
    
    #this is function to insert node at the begging of linked list -->
    def insertbeg(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    
        
o=Linkedlist()
o.insertbeg(10)
o.insertbeg(100)
o.insertbeg(1000)
o.insertbeg(100000)
o.printall()

    
        
        