class Stack:
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
        self.left=lchild
        self.data=newdata
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
    def preorder(self):
        st=Stack()
        st.push(None)
        curnode=self.root
        while curnode is not None:
            print(curnode.data,end=" ")
            if curnode.right:
                st.push(curnode.right)
            if curnode.left:
                curnode=curnode.left
            else:
                curnode=st.pop()
    def inorder(self):
        st=Stack()
        st.push(None)
        curnode=self.root
        while curnode is not None:
            while curnode is not None:
                st.push(curnode)
                curnode=curnode.left
            curnode=st.pop()
            flag=True
            while curnode is not None and flag is True:
                print(curnode.data, end=" ")
                if curnode.right:
                    curnode=curnode.right
                    flag=False
                else:
                    curnode=st.pop()
bst=BST()
while True:
    print("\nProgram to Implement binary search tree")
    print("\t1.Insert Node")
    print("\t2.Preorder traversal")
    print("\t3.Inorder traversal")
    print("\t4.Exit")
    ch=int(input("Enter your choice: "))
    if ch == 1:
        num=int(input("Enter the Data: "))
        bst.insert(num)
    elif ch == 2:
        print("PreOrder: ",end=' ')
        bst.preorder()
    elif ch == 3:
        print("InOrder: ",end=' ')
        bst.inorder()
    elif ch == 4:
        print("\nQuiting.....")
        break
    else:
        print("Invalid choice...Please Enter Correct Choice")
        continue      