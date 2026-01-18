class create_queue:
    def __init__(self):
        self.queue=[]
    def IsEmpty(self):
        if self.queue==[]:
            return True
        else:
            return False
    def Enqueue(self,num):
        self.queue.append(num)
    def Dequeue(self):
        if self.IsEmpty():
            return "Underflow Occur"
        else:   
            return self.queue.pop(0)
    def peek(self):
        if self.IsEmpty():
            return "Underflow Occur"
        else:
            return self.queue[0]
    def Display(self):
        if self.IsEmpty():
            print("Underflow Occur")
        else:
            print(self.queue)
obj=create_queue()
while(1):
    print("1: To enque element !!!!")
    print("2: To deque element !!!")
    print("3: To peek element !!!")
    print("4: To display queue !!!")
    print("5: To stop !!!")
    a=int(input("Enter Any Number between the list : "))
    if a==1:
        x=int(input("Enter any number : "))
        obj.Enqueue(x)
    elif a == 2:
        print(obj.Dequeue())
    elif a == 3:
        print(obj.peek())
    elif a == 4:
        obj.Display()
    elif a == 5 or a>5 or a<1 :
        break