class DNode:
    def __init__(self,newdata=None,plink=None,nlink=None):
        self.data=newdata
        self.prev=plink
        self.next=nlink
class DLL:
    def __init__(self):
        self.head=None
    def insert_end(self,newdata):
        newnode=DNode(newdata)
        if self.head is None:
            self.head=newnode
        else:
            curnode=self.head
            while curnode.next is not None:
                curnode=curnode.next
            newnode.prev=curnode
            newnode.next=curnode.next
            if curnode.next is not None:
                curnode.next.prev=newnode
            curnode.next=newnode
    def insert_end(self,newdata):
        newnode=DNode(newdata,None,self.head)
        if self.head is not None:
            self.head.prev=newnode
        self.head=newnode
    def insert_nth(self,newdata,posn):
        newnode=DNode(newdata)
        if posn == 1:
            newnode.next=self.head
            if self.head is not None:
                self.head.prev=newnode
            self.head=newnode
        else:
            curnode=self.head
            while curnode <= posn-2 and curnode.next is not None:
                curnode=curnode.next
            newnode.prev=curnode
            newnode.next=curnode.next
            if curnode.next is not None:
                curnode.next.prev=newnode
            curnode.next=newnode
        