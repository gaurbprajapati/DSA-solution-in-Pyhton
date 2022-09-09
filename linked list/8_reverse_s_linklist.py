# from typing import NewType


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None
        
    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
            
    def reverseLinkedlist(self):
        previous = None
        current=self.head
        while(current!=None):
            n_=current.next
            current.next=previous
            previous=current
            current=n_
        self.head=previous

    
    def print_all(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
            
o=Linkedlist()
o.insertend(90)
o.insertend(30)
o.insertend(10)
o.insertend(20)
print("The normal linkedlist:-000")
o.print_all()       
print("The reverse linked list:-")
o.reverseLinkedlist()       
o.print_all()
        
        