#Fibonacci Series...
#[0  1  1  2  3  5  8  13  21 ..... ]
n=int(input("Enter a number : "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    count=a+b
    print(count,end=" ")
    a=b
    b=count
