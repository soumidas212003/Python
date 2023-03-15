#1*2*3*4*5
def factorial(n):
    c=1
    for i in range(1,n+1):
        c*=i
    return c  
n=int(input("Enter a number : "))
print("Factorial of ",n,"is",factorial(n)) 