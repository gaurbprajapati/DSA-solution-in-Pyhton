class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    # this to traverse the linked list -->
    def printall(self):
        if self.head == None:
            print("Linked list is empty.")
        else:
            n = self.head
            while (n is not None):
                print(n.data)
                n = n.next

    # # this is function to insert node at the begging of linked list -->
    # def insertbeg(self,data):
    #     new_node=Node(data)
    #     new_node.ref=self.head
    #     self.head=new_node

    # this is function to insert node at the end of linked list -->
    def insertend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    # <--this is function to delet the node at the beg. of linked list--->
    def delBeg(self):
        if self.head == None:
            print("The linked list is empty.")
        else:
            self.head = self.head.next

    # <--this is function to deletee the node at END of linked list-->
    def delEnd(self):
        # self.head=head
        if self.head == None:
            print("The linked list is empty.")
        if self.head.next == None:
            self.head = None
            # return None
        else:
            tm = self.head
            while(tm.next.next == None):
                # break
                tm = tm.next
                # break
            tm.next = None
    
    def removeLastNode(self):
	    if self.head == None:
	    	return None
	    if self.head.next == None:
	    	self.head = None
	    	return None
	    second_last = self.head
	    while(second_last.next.next):
	    	second_last = second_last.next
	    second_last.next = None
	    return self.head

    def del_byValue(self, value):
        tmpp = self.head
        if (tmpp != None):
            if tmpp.data == value:
                tmpp = tmpp.next
                tmpp = None
                return
        tmpp = self.head
        while(tmpp != None):
            # print(tmpp.data)
            if tmpp.data == value:
                # print("Found.........")
                break
            p=tmpp
            tmpp = tmpp.next
        if tmpp == None:
            return
            # print(f"The value node {value} is not found")
        # else:
        p.next= tmpp.next
        tmpp=None
        

    def printall(self):
        if self.head == None:
            print("Linked list is empty.")
        else:
            n = self.head
            while (n is not None):
                print(n.data)
                n = n.next




o = Linkedlist()
o.insertend(20)
o.insertend(20202)
o.insertend(5050)
o.insertend(900)
o.printall()

# o.delBeg()
# o.removeLastNode()
# o.del_byValue(20)
# o.deleteNode(5050)
o.delEnd()
print("linked list after deleting Node---")
o.printall()
