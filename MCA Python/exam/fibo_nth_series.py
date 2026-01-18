def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
r=int(input("Enter range: "))
for i in range(1,r+1):
    print(fibo(i),end=" ")