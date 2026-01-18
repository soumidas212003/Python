#x^1/1! - x^2/3! + x^3/5! .......n terms
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def iteration(x,n):
    c=1
    f=1
    sum=0
    for i in range(1,n+1):
        if c%2!=0:
            print(x,"^",i,"/",f,"!",end="-")
            sum+=(x**i)//fact(f)
        else:
           print(x,"^",i,"/",f,"!",end="+")
           sum-=(x**i)//fact(f)
        c+=1
        f+=2
    print("\b ","=",sum)
n=int(input("Enter the range of the series : "))
x=int(input("Enter the number : "))
iteration(x,n)
