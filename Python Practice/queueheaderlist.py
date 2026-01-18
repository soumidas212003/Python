class Node:
    def __init__(self,newdata,link):
        self.data=newdata
        self.next=link
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def isEmpty(self):
        return self.front is None
    def enqueue(self,newdata):
        newnode=Node(newdata,None)
        if self.front is None:
            self.front=self.rear=newnode
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        frontnode=self.front
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            self.front=frontnode.next
        return frontnode.data
    def peek(self):
        return self.front.data
    def display(self):
        curnode=self.front
        print()
        while curnode is not None:
            print(curnode.data,'->',end="")
            curnode=curnode.next
        print("None")
q=Queue () 
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
        q.enqueue(num) 
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