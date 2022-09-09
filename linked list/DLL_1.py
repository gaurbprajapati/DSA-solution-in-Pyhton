from typing import Text


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self) -> None:
        self.head = None

    def insertbeg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        self.head = new_node
        self.head.prev = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        # if self.head is None:
        #     new_node.prev = None
        #     self.head = new_node
        #     return
        tem = self.head
        while(tem.next != None):
            tem = tem.next
            # break
        tem.next = new_node
        new_node.prev = tem
        new_node.next = None

    def insert_before_value(self, value, data):
        t = self.head
        while(t != None):
            if t.data == value:
                break
            t = t.next
        if t == None:
            print(f"The linked list node {value} is not found.")
        else:
            new_node = Node(data)
            new_node.next=t
            new_node.prev=t.prev
        if t.prev!=None:
            t.prev.next=new_node
        t.prev=new_node
        
    def insert_node_after(self,data,value):
        if self.head==None:
            print("The DLL is empty")
        else:
            temp=self.head
            while(temp!=None):
                if temp.data==value:
                    break
                temp=temp.next
        if temp== None:
            print(f"The given node {value} is empty")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            new_node.pre=temp
        if temp.next!=None:
            temp.next.prev=new_node
        temp.next=new_node
            # new_node.next=t
            # t.next.prev=new_node
            # new_node.prev=t

    def printall(self):
        t = self.head
        while(t != None):
            print(t.data)
            t = t.next

    # # Adding a node at the front of the list
    # def push(self, new_data):

    # 	# 1 & 2: Allocate the Node & Put in the data
    # 	new_node = Node(data = new_data)

    # 	# 3. Make next of new node as head and previous as NULL
    # 	new_node.next = self.head
    # 	new_node.prev = None

    # 	# 4. change prev of head node to new node
    # 	if self.head is not None:
    # 		self.head.prev = new_node

    # 	# 5. move the head to point to the new node
    # 	self.head = new_node


    # # This code is contributed by jatinreaper
o = doublyLL()
o.insertbeg(10)
o.insertbeg(20)
o.insertbeg(30)
o.insertbeg(40)
o.insertEnd(90)
o.printall()
print("dd linkedlist after node deletion:-")
o.insert_node_after(4,20)
o.printall()