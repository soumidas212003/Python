#1+2+4+7+11+16...n terms
n=int(input("Enter a number : "))
c=1
sum=0
for i in range(1,n+1):
    print(c,end=" + ")
    sum+=c
    c+=i
print("\b\b=",sum)
