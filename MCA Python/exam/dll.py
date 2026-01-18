class DNode:
    def __init__(self,newdata=None,llink=None,rlink=None):
        self.data=newdata
        self.prev=llink
        self.next=rlink
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self,mydata):
        newNode=DNode(mydata)
        if self.head is None:
            self.head=newNode
        else:
            curNode=self.head
            while curNode.next is not None:
                curNode=curNode.next
            curNode.next=newNode
            newNode.prev=curNode
    def display(self):
        if self.head is None:
            print("Nothing to display..")
        else:
            curnode=self.head
            print("None<=>",end='')
            while curnode is not None:
                print(curnode.data,end="<=>")
                curnode=curnode.next
            print("None")
    def rev_display(self):
        if self.head is None:
            print("Nothing to display..")
        else: 
            curNode=self.head
            print("None<=>",end='')
            while curNode.next is not None:
                curNode=curNode.next
            while curNode is not None:
                print(curNode.data,end='<=>')
                curNode=curNode.prev
            print("None")

dll=DLL()
while True:
    print("\n1.Insert")
    print("\n2.Display")
    print("\n3.Reverse Display")
    print("\n4.Exit")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        num=int(input("Enter the number: "))
        dll.insert_end(num)
    elif ch == 2:
        dll.display()
    elif ch == 3:
        dll.rev_display()
    elif ch == 4:
        print("Quit...")
        break
    else:
        continue