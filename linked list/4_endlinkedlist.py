class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None
        
    #this to traverse the linked list -->   
    def printall(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            n=self.head
            while (n is not None):
                print(n.data)
                n=n.next
        
    # # this is function to insert node at the begging of linked list -->
    # def insertbeg(self,data):
    #     new_node=Node(data)
    #     new_node.ref=self.head
    #     self.head=new_node
    
    
        
                
    #this is function to insert node at the end of linked list -->      
    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new_node
            
o=Linkedlist()
o.insertend(20)
# o.insertbeg(10)
o.insertend(20202)
o.insertend(900)

o.printall()