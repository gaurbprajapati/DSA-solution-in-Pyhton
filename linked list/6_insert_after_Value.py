from typing import NewType


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

    
    #-->function to insert the node at the end of linked list -->
    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new_node
    
    #-->program to insert the node befor the give value of node--> 
    # def insert_befor_value(self,data,value):
    #     new_node=Node(data)
    #     if self.head==None:
    #         print("The linked list is empty.")
    #     else:
    #         temp=self.head
    #         while (temp!=None):
    #             if temp.next.data==value:
    #                 break
    #             temp=temp.next
    #         new_node.next=temp.next
    #         temp.next=new_node

    #this is function to insert node at the begging of linked list -->
    # def insertBeg(self,data):
    #     new_node=Node(data)
    #     new_node.next=self.head
    #     self.head=new_node
        
    #--->>this is function to insert the node value after the given node value
    def afterValue(self,data,value):
        # self.data=None
        if self.head==None:
            print("The givaen linked list is Empty.")
        else:
            t=self.head
            while(t!=None):
                if t.data==value:
                    break
                t=t.next
            if t is None:
                print(f"The node value {value} is not found.")
            else:
                new_node=Node(data)
                new_node.next=t.next
                t.next=new_node
  
                
        
            



o=Linkedlist()
# o.insertBeg(900)
o.insertend(2)
o.insertend(20)
# o.insert_befor_value(25,20202)
o.afterValue(90,2)
o.afterValue(900000,90)
o.afterValue(900000,20)
o.afterValue(900000,1)
o.printall()
        
        