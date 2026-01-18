class Node:
    def __init__(self,mydata=None,mylink=None):
        self.data=mydata
        self.next=mylink
class CLL:
    def __init__(self):
        self.head=None
    def insert_nth(self,mydata,posn):
        newnode=Node(mydata)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
        elif posn==1:
            curnode=self.head
            while curnode.next is not self.head:
                curnode=curnode.next
            newnode.next=self.head
            curnode.next=newnode
            self.head=newnode
        else:
            curnode=self.head
            i=1
            while i<=posn-2 and curnode.next is not self.head:
                curnode=curnode.next
            newnode.next=curnode.next
            curnode.next=newnode
    def display(self):
        if self.head is None:
            print("Null list")
        else:
            curnode=self.head
            while curnode.next is not self.head:
                print(curnode.data,end="->")
                curnode=curnode.next
            print(curnode.data)
list=CLL()
list.insert_nth(1,5)
list.display()