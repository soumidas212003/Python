#1+11+111+1111+.... upto N terms
n=int(input("Enter a number : "))
count=1
sum=0
for i in range(1,n+1):
    print(count,end="+")
    sum+=count
    count=(count*10)+1
print("\b=",sum)