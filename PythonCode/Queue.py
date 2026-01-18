def create_queue():
    queue=[]
    return queue
def Isempty(queue):
    if queue==[]:
        return True
    else:
        return False
def Enqueue(queue,num):
        queue.append(num)
def Dequeue(queue):
    if Isempty(queue):
        return "Underflow Occur"
    else:
        return queue.pop(0)
def peek(queue):
    if Isempty(queue):
        return "Underflow Occur"
    else:
        return queue[0]
def Display(queue):
    if Isempty(queue):
        print("Underflow Occur")
    else:
        print(queue)
qu=create_queue()
while(1): 
    print("1: To enque element !!!!")
    print("2: To deque element !!!")
    print("3: To peek element !!!")
    print("4: To display queue !!!")
    print("5: To stop !!!")
    a=int(input("Enter Any Number between the list : "))
    if a == 1:
        x=int(input("Enter any number : "))
        Enqueue(qu,x)
    elif a == 2:
        print(Dequeue(qu))
    elif a == 3:
        print(peek(qu))
    elif a == 4:
        Display(qu)
    elif a == 5 or a>5 or a<1 :
        break