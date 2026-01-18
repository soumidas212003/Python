#all recursive function is here
def pow(base,exp):
    if exp==0:
        return 1
    else:
        x=pow(base,exp-1)
        y=base*x
        return y
#gcd=greatest common divisior/Hcf=Highest common Factor
#15=1,3,5,15
#8=1,2,4,8
def gcd(a,b):
    if b==0:
        return a
    else:
        temp=a%b
        return gcd(b,temp)
#fibonacci using recursion
def fibo(a,b,n):
    if n==0:
        return
    else:
        c=a+b
        print(c,end=" ")
        fibo(b,c,n-1)
#Factorial using recursion
def facto(n):
    if n==0 or n==1:
        return 1
    else:
        x=facto(n-1)
        y=n*x
        return y