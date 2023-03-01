#Fibonacci Series...
#[0  1  1  2  3  5  8  13  21 ..... ]
n=int(input("Enter a number : "))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    count=a+b
    a=b
    b=count
