class stack:
    def __init__(self):
        self.mylist=[]
    def isempty(self):
        return len(self.mylist)==0
    def push(self,val):
        self.mylist.append(val)
    def pop(self):
        return self.mylist.pop()
    def peek(self):
        return self.mylist[-1]
class Node:
    def __init__(self,newdata=None,lchild=None,rchild=None):
        self.data=newdata
        self.left=lchild
        self.right=rchild
class BST:
    def __init__(self):
        self.root=None
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.root is None:
            self.root=newnode
        else:
            curnode=self.root
            parent=None
            while curnode is not None:
                parent=curnode
                if newdata<curnode.data:
                    curnode=curnode.left
                else:
                    curnode=curnode.right
            if newdata<parent.data:
                parent.left=newnode
            else:
                parent.right=newnode