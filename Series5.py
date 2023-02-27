#2+5+8+11+14+ ........ upto N terms
n=int(input("Enter a number : "))
count=2
sum=0
for i in range(1,n+1):
    print(count,end="+")
    sum+=count
    count+=3
print("\b=",sum)