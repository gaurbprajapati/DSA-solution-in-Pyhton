class Node:
    def __init__(self,data) -> None:
        self.data=data
        # self.ref=None
        self.next=None

class create:
    def __init__(self) -> None:
        self.head=None
    def create(self):
        self.head=None
        while (True):
            n_node=Node(data)
            self.data=int(input("enter value to insert:-"))
            if self.head==None:
                self.head=n_node
            else:
                temp.next=n_node
            