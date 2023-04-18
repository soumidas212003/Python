class create_stack:
    def __init__(self):
        self.stack=[]
    def IsEmpty(self):
        if self.stack==[]:
            return True
        else:
            return False
    def push(self,num):
        self.stack.append(num)    
    def pop(self):
        if self.IsEmpty():
            return "Underflow occur"
        else:
            return self.stack.pop()
    def peek(self):
        if self.IsEmpty():
            return "Underflow occur"
        else:
            return self.stack[-1]
    def Display(self):
        if self.IsEmpty():
            print("Underflow occur")
        else:
            print (self.stack[::-1])
obj=create_stack()
while(1):
    print("1: To push element !!!!")
    print("2: To pop element !!!")
    print("3: To peek element !!!")
    print("4: To display Stack !!!")
    print("5: To stop !!!")
    a=int(input("Enter Any Number between the list : "))
    if a == 1:
        n=int(input("Enter any number you want to push: "))
        obj.push(n)
    elif a == 2:
        print(obj.pop())
    elif a == 3:
        print(obj.peek())
    elif a == 4:
        obj.Display()
    elif a == 5 or a>5 or a<1 :
        break