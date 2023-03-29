def create_stack():
    stack=[]
    return stack
def Isempty(stack):
    if stack==[]:
        return True
    else:
        return False
def push(stack,num):
        stack.append(num)
def pop(stack):
    if Isempty(stack):
        return "Underflow Occur"
    else:
        return stack.pop()
def peek(stack):
    if Isempty(stack):
        return "Underflow Occur"
    else:
        return stack[-1]
def Display(stack):
    if Isempty(stack):
        print("Underflow Occur")
    else:
        print(stack[::-1])
st=create_stack()
while(1): 
    print("1: To push element !!!!")
    print("2: To pop element !!!")
    print("3: To peek element !!!")
    print("4: To display Stack !!!")
    print("5: To stop !!!")
    a=int(input("Enter Any Number between the list : "))
    if a == 1:
        x=int(input("Enter any number : "))
        push(st,x)
    elif a == 2:
        print(pop(st))
    elif a == 3:
        print(peek(st))
    elif a == 4:
        Display(st)
    elif a == 5 or a>5 or a<1 :
        break