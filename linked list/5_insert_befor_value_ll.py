class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None
        
    def printall(self):
        if self.head is None:
            print("The given linked list is empty.")
        else:
            n=self.head
            while(n is not None):
                print(n.data)
                n=n.next

    
     
    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new_node
            
    def insert_befor_value(self,data,value):
        new_node=Node(data)
        if self.head==None:
            print("The linked list is empty.")
        else:
            temp=self.head
            while (temp!=None):
                if temp.next.data==value:
                    break
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
            



o=Linkedlist()
o.insertend(20)
o.insertend(20202)
o.insertend(900)
o.insert_befor_value(25,20202)

o.printall()
        
        