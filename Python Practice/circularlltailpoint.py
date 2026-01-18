class Node:
    def __init__(self,newdata,link):
        self.data=newdata
        self.next=link
class Queue:
    def __init__(self):
        self.tail=None
    def isEmpty(self):
        return self.tail is None
    def Enqueue(self,newdata):
        newnode=Node(newdata,None)
        if self.tail is None:
            newnode.next=newnode
        else:
            newnode.next=self.tail.next
            self.tail.next=newnode
        self.tail=newnode
    def peek(self):
        return self.tail.next.data
    def dequeue(self):
        frontNode=self.tail.next
        if frontNode.next==frontNode:
            self.tail=None
        else:
            self.tail.next=frontNode.next
        return frontNode.data
    def display(self):
        curnode=self.tail.next
        print()
        while curnode is not self.tail:
            print(curnode.data,'->',end="")
            curnode = curnode.next 
        print(curnode.data)

q=Queue()
while (True):
    print("\nPROGRAM TO IMPLEMENT QUEUE") 
    print("==============================") 
    print("\tl. Enqueue") 
    print("\t2. Dequeue") 
    print("\t3. Peek") 
    print("\t4. Display") 
    print("\t5. Exit") 
    print("===============================") 
    choice=int(input("Enter your Choice: ")) 
    if choice==1: 
        num=int(input("Enter the Data: ")) 
        q.Enqueue(num) 
    elif choice==2: 
        if q.isEmpty(): 
            print("Queue Underflow") 
        else: 
            num=q.dequeue() 
            print("Item dequeued = ", num) 
    elif choice==3: 
        if q.isEmpty(): 
            print("Queue Underflow") 
        else: 
            num=q.peek() 
            print("Item at the front of the Queue = ", num) 
    elif choice==4 : 
        if q.isEmpty() : 
            print("Queue is Empty") 
        else: 
            q.display() 
    elif choice==5 : 
        print("\nQuiting...") 
        break 
    else: 
        print("Invalid choice. Please Enter Correct Choice") 
        continue