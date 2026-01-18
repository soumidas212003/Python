#1+2+4+7+11+16+... upto N terms
n=int(input("Enter a number : "))
count=1
sum=0
for i in range(1,n+1):
    print(count,end="+")
    sum+=count
    count+=i 
print("\b=",sum)