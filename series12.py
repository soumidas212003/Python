#Fibonacci Series...upto N
n=int(input("Enter the range of the series:- "))
a=0
b=1
c=0
while c<=n:
    print(c,end=" ")
    a=b
    b=c
    c=a+b