class DNode:
    def __init__(self,newdata=None,plink=None,nlink=None):
        self.data=newdata
        self.previous=plink
        self.next=nlink
class DLL:
    def __init__(self):
        self.head=None
    def insertend(self,newdata):
        newnode=DNode(newdata)
        if self.head is None:
            self.head=newnode
        else:
            curnode=self.head
            while curnode.next is not None:
                curnode=curnode.next
            curnode.next=newnode
            newnode.previous=curnode
    def insertbeg(self,newdata):
        newnode=DNode(newdata,None,self.head)
        if self.head is not None:
            self.head.previous=newnode
        self.head=newnode
    def display(self):
        curnode=self.head
        if self.head is None:
            print("Empty list..")
        else:
            print("None",end="<=>")
            while curnode is not None:
                print(curnode.data,end="<=>")
                curnode=curnode.next
            print("None")
    def revdisplay(self):
        if self.head is None:
            print("Empty list...")
        else:
            curnode=self.head
            print("None",end="<=>")
            while curnode.next is not None:
                curnode=curnode.next
            while curnode is not None:
                print(curnode.data,end="<=>")
                curnode=curnode.previous
            print(None)
    def deletefirst(self):
        if self.head is None:
            print("Delete Not possible..")
        else:
            curnode=self.head
            self.head=curnode.next
            if self.head is not None:
                self.head.previous=None
            del(curnode)
            print("Node Deleted Successfully..")
    def deletelast(self):
        if self.head is None:
            print("Deletion not possible..")
        elif self.Head.next is None:
            del(self.Head)
            self.Head=None
        else:
            curnode=self.head
            while curnode.next.next is not None:
                curnode=curnode.next
            del(curnode.next)
            curnode.next=None
            print("Node deleted successfully")
    def insertnth(self,newdata,posn):
        newnode=DNode(newdata)
        curnode=self.head
        if posn == 1:
            newnode.next=self.head
            if self.head is not None:
                self.head.previous=newnode
            self.head=newnode
        else:
            c=1
            while c<=posn-2 and curnode.next is not None:
                c+=1
                curnode=curnode.next
            newnode.next=curnode.next
            newnode.previous=curnode
            if curnode.next is not None:
                curnode.next.previous=newnode
            curnode.next=newnode
    def deletenth(self,posn):
        if self.head is None:
            print("Deletion not possible...")
        else:
            curnode=self.head
            if posn==1:
                self.head=curnode.next
                del(curnode)
                if self.head is not None:
                    self.head.previous=None
                print("Node Deleted successfully")
            else:
                c=1
                while c<=posn-2 and curnode.next is not None:
                    c+=1
                    curnode=curnode.next
                if curnode.next is None:
                    print("Node not found...")
                else:
                    temp=curnode.next
                    curnode.next=temp.next
                    if temp.next is not None:
                        temp.next.previous=curnode
                    del(temp)
                    print("Node deleted Successfully...")

dll = DLL()
while True:
    print("\nPROGRAM TO IMPLEMENT DOUBLY LINKED LIST")
    print("========================================")
    print("1. Create / Append The List")
    print("2. Insert Node At Beginning")
    print("3. Insert Node at Nth Position")
    print("4. Delete First Node")
    print("5. Delete Last Node")
    print("6. Delete Nth Node")
    print("7. Displaying the List")
    print("8. Displaying the List in Reverse Order")
    print("9. Exit")
    print("========================================")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        opt = 'Y'
        while opt.upper() == 'Y':
            num = int(input("Enter the Data: "))
            dll.insertend(num)
            opt = input("Enter more (y/n): ")
    elif choice == 2:
        num = int(input("Enter the Data: "))
        dll.insertbeg(num)
    elif choice == 3:
        loc = int(input("Enter The Node number Before which new node will be inserted: "))
        num = int(input("Enter the Data: "))
        dll.insertnth(num, loc)
    elif choice == 4:
        dll.deletefirst()
    elif choice == 5:
        dll.deletelast()
    elif choice == 6:
        num = int(input("Enter The Node Number You Want To Delete: "))
        dll.deletenth(num)
    elif choice == 7:
        dll.display()
    elif choice == 8:
        dll.revdisplay()
    elif choice == 9:
        print("\nQuitting.......")
        break
    else:
        print("Invalid choice. Please Enter Correct Choice")
        continue
