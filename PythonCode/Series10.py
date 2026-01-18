#1-3+5-7+9..................N terms
n=int(input("Enter a number : "))
sum=0
count=1
for i in range(1,n+1):
    print(count,end="")
    if i%2!=0:
        print("-",end="")
        sum-=count
    else:
        print("+",end="")
        sum+=count
    count+=2
print ("\b")
    